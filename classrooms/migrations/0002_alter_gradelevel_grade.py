# Generated by Django 5.1.1 on 2024-10-23 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classrooms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gradelevel',
            name='grade',
            field=models.CharField(choices=[('Grade 9', 'Grade 9'), ('Grade 11', 'Grade 11'), ('Grade 7', 'Grade 7'), ('Grade 12', 'Grade 12'), ('Grade 8', 'Grade 8'), ('Transitioning', 'Transitioning'), ('Grade 10', 'Grade 10')], max_length=20, unique=True),
        ),
    ]
