# Generated by Django 5.1.1 on 2024-10-29 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0010_alter_student_household_income_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='household_income',
            field=models.CharField(blank=True, choices=[('from Php 18,000 - Php 35,000', 'from Php 18,000 - Php 35,000'), ('below Php 9,000', 'below Php 9,000'), ('above Php 35,000', 'above Php 35,000'), ('from Php 9,000 - Php 18,000', 'from Php 9,000 - Php 18,000')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='religion',
            field=models.CharField(choices=[('Sikhism', 'Sikhism'), ('Roman catholic', 'Roman Catholic'), ('Islam', 'Islam'), ('Hinduism', 'Hinduism'), ('Buddhism', 'Buddhism'), ('Judaism', 'Judaism'), ('Christianity', 'Christianity'), ('Other', 'Other')], default='other', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='sex',
            field=models.CharField(choices=[('Female', 'Female'), ('Male', 'Male')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='status',
            field=models.CharField(blank=True, choices=[('For Transfer', 'For Transfer'), ('For Dropout', 'For Dropout'), ('For Graduation', 'For Graduation'), ('For Retention', 'For Retention'), ('Currently Enrolled', 'Currently Enrolled'), ('For Promotion', 'For Promotion')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='strand',
            field=models.CharField(blank=True, choices=[('GAS', 'GAS'), ('IA', 'IA'), ('Not Applicable (JHS)', 'Not Applicable (JHS)'), ('BAM', 'BAM'), ('SPORTS & ARTS', 'SPORTS & ARTS'), ('HESS', 'HESS'), ('TVL', 'TVL'), ('ICT', 'ICT'), ('STEM', 'STEM'), ('HE', 'HE')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='transfer_status',
            field=models.CharField(blank=True, choices=[('Transferred In', 'Transferred In'), ('Regular', 'Regular'), ('Moved In', 'Moved In')], default='Regular', max_length=15, null=True),
        ),
    ]
