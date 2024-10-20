# Generated by Django 5.1.1 on 2024-10-20 03:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classrooms', '0003_alter_gradelevel_grade'),
        ('students', '0002_alter_student_lrn_alter_student_household_income_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='classroom',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='classrooms.classroom', verbose_name='Classrooms'),
        ),
        migrations.AlterField(
            model_name='student',
            name='household_income',
            field=models.CharField(blank=True, choices=[('from Php 9,000 - Php 18,000', 'from Php 9,000 - Php 18,000'), ('from Php 18,000 - Php 35,000', 'from Php 18,000 - Php 35,000'), ('below Php 9,000', 'below Php 9,000'), ('above Php 35,000', 'above Php 35,000')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='is_4ps',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='student',
            name='religion',
            field=models.CharField(choices=[('Buddhism', 'Buddhism'), ('Hinduism', 'Hinduism'), ('Other', 'Other'), ('Roman catholic', 'Roman Catholic'), ('Sikhism', 'Sikhism'), ('Islam', 'Islam'), ('Christianity', 'Christianity'), ('Judaism', 'Judaism')], default='other', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='sem',
            field=models.CharField(blank=True, choices=[('1st Semester', '1st Semester'), ('Yearly', 'Yearly'), ('2nd Semester', '2nd Semester')], default='None', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='status',
            field=models.CharField(blank=True, choices=[('For Transfer', 'For Transfer'), ('For Dropout', 'For Dropout'), ('Currently Enrolled', 'Currently Enrolled'), ('For Retention', 'For Retention'), ('For Promotion', 'For Promotion'), ('For Graduation', 'For Graduation')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='strand',
            field=models.CharField(blank=True, choices=[('IA', 'IA'), ('TVL', 'TVL'), ('BAM', 'BAM'), ('Not Applicable (JHS)', 'Not Applicable (JHS)'), ('HE', 'HE'), ('STEM', 'STEM'), ('SPORTS & ARTS', 'SPORTS & ARTS'), ('HESS', 'HESS'), ('GAS', 'GAS'), ('ICT', 'ICT')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='transfer_status',
            field=models.CharField(blank=True, choices=[('Transferred In', 'Transferred In'), ('Regular', 'Regular'), ('Moved In', 'Moved In')], default='Regular', max_length=15, null=True),
        ),
    ]
