# Generated by Django 2.0.5 on 2018-05-26 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20180526_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='student',
            field=models.ForeignKey(default='', on_delete='SET_NULL', related_name='grade_student', to='core.Student'),
        ),
    ]
