# Generated by Django 5.1.1 on 2024-10-23 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_teacher_rank'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='rank',
            field=models.CharField(choices=[('Teacher III', 'Teacher III'), ('Teacher II', 'Teacher II'), ('Master Teacher I', 'Master Teacher I'), ('Teacher VII', 'Teacher VII'), ('Teacher V', 'Teacher V'), ('Teacher IV', 'Teacher IV'), ('Master Teacher IV', 'Master Teacher IV'), ('Master Teacher III', 'Master Teacher III'), ('Teacher I', 'Teacher I'), ('Teacher VI', 'Teacher VI'), ('Master Teacher II', 'Master Teacher II')], default='None', max_length=30),
        ),
    ]
