# Generated by Django 5.1.1 on 2024-10-23 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classrooms', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gradelevel',
            name='grade',
        ),
        migrations.AddField(
            model_name='gradelevel',
            name='gradelevel',
            field=models.CharField(choices=[('Grade 12', 'Grade 12'), ('Grade 8', 'Grade 8'), ('Transitioning', 'Transitioning'), ('Grade 11', 'Grade 11'), ('Grade 7', 'Grade 7'), ('Grade 9', 'Grade 9'), ('Grade 10', 'Grade 10')], default=None, max_length=20, unique=True),
        ),
    ]
