# Generated by Django 5.1.1 on 2024-10-25 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_alter_student_household_income_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='household_income',
            field=models.CharField(blank=True, choices=[('above Php 35,000', 'above Php 35,000'), ('below Php 9,000', 'below Php 9,000'), ('from Php 18,000 - Php 35,000', 'from Php 18,000 - Php 35,000'), ('from Php 9,000 - Php 18,000', 'from Php 9,000 - Php 18,000')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='religion',
            field=models.CharField(choices=[('Other', 'Other'), ('Roman catholic', 'Roman Catholic'), ('Buddhism', 'Buddhism'), ('Christianity', 'Christianity'), ('Sikhism', 'Sikhism'), ('Judaism', 'Judaism'), ('Islam', 'Islam'), ('Hinduism', 'Hinduism')], default='other', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='sex',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='status',
            field=models.CharField(blank=True, choices=[('For Dropout', 'For Dropout'), ('For Graduation', 'For Graduation'), ('For Retention', 'For Retention'), ('Currently Enrolled', 'Currently Enrolled'), ('For Promotion', 'For Promotion'), ('For Transfer', 'For Transfer')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='strand',
            field=models.CharField(blank=True, choices=[('HESS', 'HESS'), ('TVL', 'TVL'), ('SPORTS & ARTS', 'SPORTS & ARTS'), ('GAS', 'GAS'), ('STEM', 'STEM'), ('IA', 'IA'), ('Not Applicable (JHS)', 'Not Applicable (JHS)'), ('BAM', 'BAM'), ('HE', 'HE'), ('ICT', 'ICT')], max_length=50, null=True),
        ),
    ]
