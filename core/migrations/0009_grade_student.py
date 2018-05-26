# Generated by Django 2.0.5 on 2018-05-26 15:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_remove_grade_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='grade',
            name='student',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='grade_student', to='core.Student'),
        ),
    ]
