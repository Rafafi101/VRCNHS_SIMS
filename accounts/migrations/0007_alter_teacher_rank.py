# Generated by Django 5.1.1 on 2024-10-23 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_teacher_rank'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='rank',
            field=models.CharField(choices=[('Master Teacher IV', 'Master Teacher IV'), ('Teacher IV', 'Teacher IV'), ('Teacher II', 'Teacher II'), ('Master Teacher I', 'Master Teacher I'), ('Master Teacher II', 'Master Teacher II'), ('Teacher V', 'Teacher V'), ('Teacher I', 'Teacher I'), ('Teacher III', 'Teacher III'), ('Teacher VII', 'Teacher VII'), ('Master Teacher III', 'Master Teacher III'), ('Teacher VI', 'Teacher VI')], default='None', max_length=30),
        ),
    ]
