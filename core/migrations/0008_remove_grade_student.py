# Generated by Django 2.0.5 on 2018-05-26 14:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20180526_1454'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grade',
            name='student',
        ),
    ]
