# Generated by Django 5.1.1 on 2024-10-23 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_alter_student_household_income_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='household_income',
            field=models.CharField(blank=True, choices=[('above Php 35,000', 'above Php 35,000'), ('from Php 18,000 - Php 35,000', 'from Php 18,000 - Php 35,000'), ('from Php 9,000 - Php 18,000', 'from Php 9,000 - Php 18,000'), ('below Php 9,000', 'below Php 9,000')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='religion',
            field=models.CharField(choices=[('Other', 'Other'), ('Christianity', 'Christianity'), ('Sikhism', 'Sikhism'), ('Judaism', 'Judaism'), ('Islam', 'Islam'), ('Hinduism', 'Hinduism'), ('Roman catholic', 'Roman Catholic'), ('Buddhism', 'Buddhism')], default='other', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='sem',
            field=models.CharField(blank=True, choices=[('Yearly', 'Yearly'), ('1st Semester', '1st Semester'), ('2nd Semester', '2nd Semester')], default='None', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='status',
            field=models.CharField(blank=True, choices=[('For Dropout', 'For Dropout'), ('For Retention', 'For Retention'), ('For Graduation', 'For Graduation'), ('For Promotion', 'For Promotion'), ('Currently Enrolled', 'Currently Enrolled'), ('For Transfer', 'For Transfer')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='strand',
            field=models.CharField(blank=True, choices=[('STEM', 'STEM'), ('BAM', 'BAM'), ('SPORTS & ARTS', 'SPORTS & ARTS'), ('GAS', 'GAS'), ('TVL', 'TVL'), ('Not Applicable (JHS)', 'Not Applicable (JHS)'), ('ICT', 'ICT'), ('HESS', 'HESS'), ('HE', 'HE'), ('IA', 'IA')], max_length=50, null=True),
        ),
    ]
