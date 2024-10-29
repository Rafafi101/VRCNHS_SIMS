# Generated by Django 5.1.1 on 2024-10-28 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0018_alter_teacher_rank'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='rank',
            field=models.CharField(choices=[('Teacher VI', 'Teacher VI'), ('Teacher V', 'Teacher V'), ('Teacher I', 'Teacher I'), ('Teacher VII', 'Teacher VII'), ('Teacher III', 'Teacher III'), ('Master Teacher II', 'Master Teacher II'), ('Master Teacher III', 'Master Teacher III'), ('Teacher IV', 'Teacher IV'), ('Teacher II', 'Teacher II'), ('Master Teacher I', 'Master Teacher I'), ('Master Teacher IV', 'Master Teacher IV')], default='None', max_length=30),
        ),
    ]