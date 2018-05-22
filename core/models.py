from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.mail import send_mail
from smart_selects.db_fields import ChainedForeignKey
from smart_selects.db_fields import ChainedManyToManyField
from django.db import models


import datetime

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    identity_number = models.IntegerField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    is_claimed = models.BooleanField(default=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = 'identity_number'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def __str__(self):
        return str(self.identity_number)


class Classroom(models.Model):
    class_id = models.AutoField(primary_key=True)
    class_name= models.CharField(max_length = 20)
    # students = models.ManyToManyField('Student', through= 'StudClass', related_name='classroom_students')
    def __str__(self):
        return str(self.class_name)


class Student(models.Model):
    name = models.CharField(max_length = 56)
    phone_number = models.CharField(max_length=15)
    semester_average = models.CharField(max_length=10)
    classroom = models.ForeignKey('core.Classroom', related_name='student_classroom',default = "", on_delete="SET_NULL")
    class Meta:
        db_table = 'students'

    def __str__(self):
        return str(self.name)


class StudClass(models.Model):
    studclass_id = models.AutoField(primary_key=True)
    classroom = models.ForeignKey('core.Classroom', related_name= 'attendance_classroom', default="", on_delete="SET_NULL") 
    student = ChainedForeignKey(
        Student,
        chained_field="classroom",
        chained_model_field="classroom",)

    
    ATTENDANCE_OUTCOME = (
        ('present', 'Present'),
        ('late', 'Late'),
        ('absent', 'Absent'),
    )
    daily_attendance = models.CharField(max_length=20, choices=ATTENDANCE_OUTCOME)
    date = models.DateField()

    def __str__(self):
        return str(self.date)


class Attendance(models.Model):
    ATTENDANCE_OUTCOME = (
        ('present', 'Present'),
        ('late', 'Late'),
        ('absent', 'Absent'),
    )
    # BEHAVIOR_OUTCOME = (
    #     ('normal', 'Normal'),
    #     ('problematic', 'Problematic'),
    # )
    daily_attendance = models.CharField(max_length=20, choices=ATTENDANCE_OUTCOME)
    # behavior = models.CharField(max_length=15, choices=BEHAVIOR_OUTCOME, default='normal')
    date = models.DateField()

    
    # student = ChainedManyToManyField( 
    #     Student,
    #     horizontal=True,
    #     verbose_name='student',
    #     chained_field="classrooms",
    #     chained_model_field="classrooms")
    
        
    # class Admin:
    #     list_filter = ('classroom__student__name',)


    def __str__(self):
        return str(self.date)


class Subject(models.Model):
    user = models.ForeignKey(
        'core.User', related_name='subjects', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    
    def __str__(self):
        return self.title


class List(models.Model):
    subject = models.ForeignKey('core.Subject', related_name= 'lists', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Task(models.Model):
    lists = models.ForeignKey('core.List', related_name= 'tasks', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


