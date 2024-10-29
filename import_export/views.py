from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from tablib import Dataset
from dateutil import parser as date_parser
import tablib
from students.models import Student
from classrooms.models import Classroom
import datetime


def import_students(request):
    if request.method == 'POST':
        dataset = Dataset()
        new_student_file = request.FILES['myfile']

        # Check if the uploaded file is an Excel file
        if not new_student_file.name.endswith('xlsx'):
            messages.error(request, 'Please upload an Excel file only (.xlsx)')
            return redirect('import_students')

        try:
            imported_data = dataset.load(
                new_student_file.read(), format='xlsx')
            successfully_imported = 0

            # Loop over each row in the dataset
            for i, data in enumerate(imported_data, start=1):
                try:
                    # Check and sanitize the LRN field
                    LRN_value = str(data[1]).strip()
                    if LRN_value is None or not LRN_value:
                        raise ValueError(
                            f"Row {i}: LRN is empty or None. Stopping further processing.")

                    # Assuming column index 13 has classroom data
                    classroom_identifier = data[13]
                    if classroom_identifier is None:
                        raise ValueError(
                            f"Row {i}: Classroom Identifier is None. Stopping further processing.")

                    try:
                        # Get the classroom instance
                        classroom_instance = Classroom.objects.get(
                            classroom=classroom_identifier)
                    except Classroom.DoesNotExist:
                        raise ValueError(f"Row {i}: Classroom with identifier {
                                         classroom_identifier} does not exist.")

                    # Handle birthday conversion
                    if isinstance(data[7], datetime.datetime):
                        converted_bday = data[7]
                    elif data[7] and isinstance(data[7], str):
                        try:
                            converted_bday = date_parser.parse(data[7])
                        except ValueError:
                            converted_bday = None
                    else:
                        converted_bday = None

                    # Construct the student object
                    student = Student(
                        LRN=int(data[1]),  # LRN as an integer
                        last_name=data[2],
                        first_name=data[3],
                        middle_name=data[4],
                        suffix_name=data[5],
                        status=data[6],
                        birthday=converted_bday,
                        religion=data[8],
                        other_religion=data[9],
                        strand=data[10],
                        # Optional, check if empty
                        age=data[11] if data[11] else None,
                        sem=data[12],
                        classroom=classroom_instance,
                        sex=data[15],
                        birth_place=data[16],
                        mother_tongue=data[17],
                        address=data[18],
                        father_name=data[19],
                        father_contact=data[20],
                        mother_name=data[21],
                        mother_contact=data[22],
                        guardian_name=data[23],
                        guardian_contact=data[24],
                        transfer_status=data[25],
                        household_income=data[26],
                        # Optional field
                        health_bmi=data[27] if data[27] else None,
                        # Optional field
                        general_average=data[28] if data[28] else None,
                        is_working_student=bool(data[29]),
                        is_returnee=bool(data[30]),
                        is_dropout=bool(data[31]),
                        is_4ps=bool(data[32]),
                        notes=data[33],
                        # Grade 7-12 history
                        g7_school=data[36],
                        g7_schoolYear=data[37],
                        g7_section=data[38],
                        g7_general_average=data[39] if data[39] else None,
                        g7_adviser=data[40],
                        g7_adviserContact=data[41],
                        g8_school=data[43],
                        g8_schoolYear=data[44],
                        g8_section=data[45],
                        g8_general_average=data[46] if data[46] else None,
                        g8_adviser=data[47],
                        g8_adviserContact=data[48],
                        g9_school=data[50],
                        g9_schoolYear=data[51],
                        g9_section=data[52],
                        g9_general_average=data[53] if data[53] else None,
                        g9_adviser=data[54],
                        g9_adviserContact=data[55],
                        g10_school=data[57],
                        g10_schoolYear=data[58],
                        g10_section=data[59],
                        g10_general_average=data[60] if data[60] else None,
                        g10_adviser=data[61],
                        g10_adviserContact=data[62],
                        g11_school=data[64],
                        g11_schoolYear=data[65],
                        g11_section=data[66],
                        g11_general_average=data[67] if data[67] else None,
                        g11_adviser=data[68],
                        g11_adviserContact=data[69],
                        g12_school=data[71],
                        g12_schoolYear=data[72],
                        g12_section=data[73],
                        g12_general_average=data[74] if data[74] else None,
                        g12_adviser=data[75],
                        g12_adviserContact=data[76],
                    )

                    # Save the student to the database
                    student.save()
                    successfully_imported += 1
                    print(f"Row {i}: Successfully imported student:", student)

                except ValueError as ve:
                    # Log and display validation errors
                    error_message = f"Row {i}: {str(ve)}"
                    print(error_message)
                    messages.error(request, error_message)
                    break

                except IntegrityError as ie:
                    # Catch database-related errors like duplicate LRNs
                    error_message = f"Row {i}: Integrity error - {str(ie)}"
                    print(error_message)
                    messages.error(request, error_message)
                    break

                except Exception as e:
                    # Catch all other exceptions and continue processing the next student
                    error_message = f"Row {
                        i}: Error saving student data: {str(e)}"
                    print(error_message)
                    messages.error(request, error_message)
                    continue

            # Display a success message if students were imported successfully
            if successfully_imported > 0:
                messages.success(request, f"Successfully imported {
                                 successfully_imported} student(s) into the database.")

        except Exception as e:
            # If there's an error during the file load, log and display it
            print(f"Error loading student/s from the file: {str(e)}")
            messages.error(
                request, f"Error loading students from the file: {str(e)}")

        return redirect('students')

    return render(request, 'students')


def export_all_students(request):
    students = Student.objects.all()
    dataset = tablib.Dataset()
    dataset.headers = ['LRN', 'Last Name', 'First Name',
                       'Middle Name', 'Birthday', 'Classroom', 'General Average']

    for student in students:
        dataset.append([
            student.LRN,
            student.last_name,
            student.first_name,
            student.middle_name,
            student.birthday,
            student.classroom.classroom if student.classroom else 'N/A',
            student.general_average
        ])

    response = HttpResponse(dataset.export(
        'xlsx'), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="students.xlsx"'
    return response
