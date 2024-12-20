# Generated by Django 5.1.1 on 2024-10-28 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0006_alter_student_household_income_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='household_income',
            field=models.CharField(blank=True, choices=[('above Php 35,000', 'above Php 35,000'), ('from Php 9,000 - Php 18,000', 'from Php 9,000 - Php 18,000'), ('below Php 9,000', 'below Php 9,000'), ('from Php 18,000 - Php 35,000', 'from Php 18,000 - Php 35,000')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='religion',
            field=models.CharField(choices=[('Roman catholic', 'Roman Catholic'), ('Buddhism', 'Buddhism'), ('Islam', 'Islam'), ('Hinduism', 'Hinduism'), ('Other', 'Other'), ('Sikhism', 'Sikhism'), ('Judaism', 'Judaism'), ('Christianity', 'Christianity')], default='other', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='sem',
            field=models.CharField(blank=True, choices=[('1st Semester', '1st Semester'), ('Yearly', 'Yearly'), ('2nd Semester', '2nd Semester')], default='None', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='sex',
            field=models.CharField(choices=[('Female', 'Female'), ('Male', 'Male')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='status',
            field=models.CharField(blank=True, choices=[('For Promotion', 'For Promotion'), ('Currently Enrolled', 'Currently Enrolled'), ('For Retention', 'For Retention'), ('For Graduation', 'For Graduation'), ('For Dropout', 'For Dropout'), ('For Transfer', 'For Transfer')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='strand',
            field=models.CharField(blank=True, choices=[('IA', 'IA'), ('SPORTS & ARTS', 'SPORTS & ARTS'), ('Not Applicable (JHS)', 'Not Applicable (JHS)'), ('BAM', 'BAM'), ('HE', 'HE'), ('ICT', 'ICT'), ('GAS', 'GAS'), ('TVL', 'TVL'), ('STEM', 'STEM'), ('HESS', 'HESS')], max_length=50, null=True),
        ),
    ]
