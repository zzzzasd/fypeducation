# Generated by Django 2.0 on 2018-03-22 08:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20180322_0849'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='semester_avarage',
            new_name='semester_average',
        ),
    ]
