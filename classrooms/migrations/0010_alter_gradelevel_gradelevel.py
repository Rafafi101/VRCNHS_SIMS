# Generated by Django 5.1.1 on 2024-10-29 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classrooms', '0009_alter_gradelevel_gradelevel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gradelevel',
            name='gradelevel',
            field=models.CharField(choices=[('Grade 9', 'Grade 9'), ('Grade 7', 'Grade 7'), ('Grade 8', 'Grade 8'), ('Grade 11', 'Grade 11'), ('Grade 10', 'Grade 10'), ('Transitioning', 'Transitioning'), ('Grade 12', 'Grade 12')], default=None, max_length=20, unique=True),
        ),
    ]