# Generated by Django 5.1.1 on 2024-10-19 13:55

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('classrooms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('LRN', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('last_name', models.CharField(max_length=30)),
                ('first_name', models.CharField(max_length=30)),
                ('middle_name', models.CharField(blank=True, max_length=30, null=True)),
                ('suffix_name', models.CharField(blank=True, max_length=10, null=True)),
                ('status', models.CharField(blank=True, choices=[('For Retention', 'For Retention'), ('For Transfer', 'For Transfer'), ('For Graduation', 'For Graduation'), ('Currently Enrolled', 'Currently Enrolled'), ('For Dropout', 'For Dropout'), ('For Promotion', 'For Promotion')], max_length=30, null=True)),
                ('birthday', models.DateField(default=datetime.date.today, null=True)),
                ('religion', models.CharField(choices=[('Islam', 'Islam'), ('Buddhism', 'Buddhism'), ('Sikhism', 'Sikhism'), ('Other', 'Other'), ('Judaism', 'Judaism'), ('Christianity', 'Christianity'), ('Hinduism', 'Hinduism'), ('Roman catholic', 'Roman Catholic')], default='other', max_length=30, null=True)),
                ('other_religion', models.CharField(blank=True, max_length=30, null=True)),
                ('strand', models.CharField(blank=True, choices=[('TVL', 'TVL'), ('IA', 'IA'), ('HE', 'HE'), ('BAM', 'BAM'), ('Not Applicable (JHS)', 'Not Applicable (JHS)'), ('STEM', 'STEM'), ('GAS', 'GAS'), ('HESS', 'HESS'), ('ICT', 'ICT'), ('SPORTS & ARTS', 'SPORTS & ARTS')], max_length=50, null=True)),
                ('age', models.IntegerField(null=True)),
                ('sem', models.CharField(blank=True, choices=[('2nd Semester', '2nd Semester'), ('1st Semester', '1st Semester'), ('Yearly', 'Yearly')], default='None', max_length=30, null=True)),
                ('sex', models.CharField(choices=[('Female', 'Female'), ('Male', 'Male')], max_length=10, null=True)),
                ('birth_place', models.CharField(blank=True, max_length=100, null=True)),
                ('mother_tongue', models.CharField(blank=True, max_length=20, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('father_name', models.CharField(blank=True, max_length=120, null=True)),
                ('father_contact', models.CharField(blank=True, max_length=15, null=True)),
                ('mother_name', models.CharField(blank=True, max_length=120, null=True)),
                ('mother_contact', models.CharField(blank=True, max_length=15, null=True)),
                ('guardian_name', models.CharField(blank=True, max_length=120, null=True)),
                ('guardian_contact', models.CharField(blank=True, max_length=15, null=True)),
                ('transfer_status', models.CharField(blank=True, choices=[('Regular', 'Regular'), ('Transferred In', 'Transferred In'), ('Moved In', 'Moved In')], default='Regular', max_length=15, null=True)),
                ('household_income', models.CharField(blank=True, choices=[('above Php 35,000', 'above Php 35,000'), ('from Php 9,000 - Php 18,000', 'from Php 9,000 - Php 18,000'), ('below Php 9,000', 'below Php 9,000'), ('from Php 18,000 - Php 35,000', 'from Php 18,000 - Php 35,000')], max_length=30, null=True)),
                ('is_returnee', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=5, null=True)),
                ('is_dropout', models.BooleanField(default=True)),
                ('is_working_student', models.BooleanField(default=True)),
                ('health_bmi', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('general_average', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('is_4ps', models.BooleanField(default=True)),
                ('notes', models.CharField(blank=True, max_length=300, null=True)),
                ('g7_school', models.CharField(blank=True, max_length=30, null=True)),
                ('g7_schoolYear', models.CharField(blank=True, max_length=15, null=True)),
                ('g7_section', models.CharField(blank=True, max_length=15, null=True)),
                ('g7_general_average', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('g7_adviser', models.CharField(blank=True, max_length=50, null=True)),
                ('g7_adviserContact', models.CharField(blank=True, max_length=50, null=True)),
                ('g8_school', models.CharField(blank=True, max_length=30, null=True)),
                ('g8_schoolYear', models.CharField(blank=True, max_length=15, null=True)),
                ('g8_section', models.CharField(blank=True, max_length=15, null=True)),
                ('g8_general_average', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('g8_adviser', models.CharField(blank=True, max_length=50, null=True)),
                ('g8_adviserContact', models.CharField(blank=True, max_length=50, null=True)),
                ('g9_school', models.CharField(blank=True, max_length=30, null=True)),
                ('g9_schoolYear', models.CharField(blank=True, max_length=15, null=True)),
                ('g9_section', models.CharField(blank=True, max_length=15, null=True)),
                ('g9_general_average', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('g9_adviser', models.CharField(blank=True, max_length=50, null=True)),
                ('g9_adviserContact', models.CharField(blank=True, max_length=50, null=True)),
                ('g10_school', models.CharField(blank=True, max_length=30, null=True)),
                ('g10_schoolYear', models.CharField(blank=True, max_length=15, null=True)),
                ('g10_section', models.CharField(blank=True, max_length=15, null=True)),
                ('g10_general_average', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('g10_adviser', models.CharField(blank=True, max_length=50, null=True)),
                ('g10_adviserContact', models.CharField(blank=True, max_length=50, null=True)),
                ('g11_school', models.CharField(blank=True, max_length=30, null=True)),
                ('g11_schoolYear', models.CharField(blank=True, max_length=15, null=True)),
                ('g11_section', models.CharField(blank=True, max_length=15, null=True)),
                ('g11_general_average', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('g11_adviser', models.CharField(blank=True, max_length=50, null=True)),
                ('g11_adviserContact', models.CharField(blank=True, max_length=50, null=True)),
                ('g12_school', models.CharField(blank=True, max_length=30, null=True)),
                ('g12_schoolYear', models.CharField(blank=True, max_length=15, null=True)),
                ('g12_section', models.CharField(blank=True, max_length=15, null=True)),
                ('g12_general_average', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('g12_adviser', models.CharField(blank=True, max_length=50, null=True)),
                ('g12_adviserContact', models.CharField(blank=True, max_length=50, null=True)),
                ('previous_section', models.CharField(blank=True, max_length=30, null=True)),
                ('classroom', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='classrooms.classroom', verbose_name='Classrooms')),
            ],
            options={
                'verbose_name_plural': 'Students',
            },
        ),
    ]
