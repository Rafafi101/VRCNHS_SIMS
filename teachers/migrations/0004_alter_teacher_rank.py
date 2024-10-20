# Generated by Django 5.1.1 on 2024-10-20 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0003_alter_teacher_rank'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='rank',
            field=models.CharField(choices=[('Master Teacher II', 'Master Teacher II'), ('Teacher VI', 'Teacher VI'), ('Teacher III', 'Teacher III'), ('Teacher VII', 'Teacher VII'), ('Teacher I', 'Teacher I'), ('Teacher V', 'Teacher V'), ('Teacher II', 'Teacher II'), ('Master Teacher IV', 'Master Teacher IV'), ('Teacher IV', 'Teacher IV'), ('Master Teacher III', 'Master Teacher III'), ('Master Teacher I', 'Master Teacher I')], default='None', max_length=30),
        ),
    ]