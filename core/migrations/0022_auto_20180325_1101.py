# Generated by Django 2.0 on 2018-03-25 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_auto_20180325_0602'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendance',
            name='student',
        ),
        migrations.AddField(
            model_name='attendance',
            name='students',
            field=models.ManyToManyField(to='core.Student'),
        ),
    ]