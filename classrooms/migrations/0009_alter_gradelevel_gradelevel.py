# Generated by Django 5.1.1 on 2024-10-28 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classrooms', '0008_alter_gradelevel_gradelevel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gradelevel',
            name='gradelevel',
            field=models.CharField(choices=[('Grade 8', 'Grade 8'), ('Transitioning', 'Transitioning'), ('Grade 11', 'Grade 11'), ('Grade 10', 'Grade 10'), ('Grade 12', 'Grade 12'), ('Grade 9', 'Grade 9'), ('Grade 7', 'Grade 7')], default=None, max_length=20, unique=True),
        ),
    ]
