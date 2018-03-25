# Generated by Django 2.0 on 2018-03-22 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20180322_0752'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attendance',
            old_name='attendance',
            new_name='daily_attendance',
        ),
        migrations.AlterField(
            model_name='attendance',
            name='behavior',
            field=models.CharField(choices=[('normal', 'Normal'), ('problematic', 'Problematic')], default='normal', max_length=15),
        ),
    ]