# Generated by Django 5.1.1 on 2024-10-28 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0007_alter_student_household_income_and_more'),
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
            field=models.CharField(choices=[('Islam', 'Islam'), ('Hinduism', 'Hinduism'), ('Other', 'Other'), ('Christianity', 'Christianity'), ('Judaism', 'Judaism'), ('Sikhism', 'Sikhism'), ('Roman catholic', 'Roman Catholic'), ('Buddhism', 'Buddhism')], default='other', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='sem',
            field=models.CharField(blank=True, choices=[('2nd Semester', '2nd Semester'), ('Yearly', 'Yearly'), ('1st Semester', '1st Semester')], default='None', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='sex',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='status',
            field=models.CharField(blank=True, choices=[('For Promotion', 'For Promotion'), ('For Retention', 'For Retention'), ('For Transfer', 'For Transfer'), ('Currently Enrolled', 'Currently Enrolled'), ('For Graduation', 'For Graduation'), ('For Dropout', 'For Dropout')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='strand',
            field=models.CharField(blank=True, choices=[('TVL', 'TVL'), ('Not Applicable (JHS)', 'Not Applicable (JHS)'), ('HESS', 'HESS'), ('IA', 'IA'), ('STEM', 'STEM'), ('ICT', 'ICT'), ('BAM', 'BAM'), ('SPORTS & ARTS', 'SPORTS & ARTS'), ('GAS', 'GAS'), ('HE', 'HE')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='transfer_status',
            field=models.CharField(blank=True, choices=[('Regular', 'Regular'), ('Moved In', 'Moved In'), ('Transferred In', 'Transferred In')], default='Regular', max_length=15, null=True),
        ),
    ]
