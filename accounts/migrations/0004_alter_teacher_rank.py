# Generated by Django 5.1.1 on 2024-10-23 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_teacher_rank'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='rank',
            field=models.CharField(choices=[('Master Teacher I', 'Master Teacher I'), ('Teacher III', 'Teacher III'), ('Teacher I', 'Teacher I'), ('Master Teacher III', 'Master Teacher III'), ('Master Teacher II', 'Master Teacher II'), ('Teacher VI', 'Teacher VI'), ('Teacher IV', 'Teacher IV'), ('Master Teacher IV', 'Master Teacher IV'), ('Teacher II', 'Teacher II'), ('Teacher V', 'Teacher V'), ('Teacher VII', 'Teacher VII')], default='None', max_length=30),
        ),
    ]
