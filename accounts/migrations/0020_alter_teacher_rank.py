# Generated by Django 5.1.1 on 2024-10-29 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0019_alter_teacher_rank'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='rank',
            field=models.CharField(choices=[('Teacher III', 'Teacher III'), ('Teacher I', 'Teacher I'), ('Master Teacher IV', 'Master Teacher IV'), ('Master Teacher II', 'Master Teacher II'), ('Master Teacher III', 'Master Teacher III'), ('Teacher V', 'Teacher V'), ('Teacher VI', 'Teacher VI'), ('Master Teacher I', 'Master Teacher I'), ('Teacher IV', 'Teacher IV'), ('Teacher II', 'Teacher II'), ('Teacher VII', 'Teacher VII')], default='None', max_length=30),
        ),
    ]