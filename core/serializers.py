from django.contrib.auth.models import Group
from rest_framework import serializers

from .models import User, Classroom, Student, Attendance, Subject, List, Task, StudClass
from drf_writable_nested import WritableNestedModelSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['identity_number', 'first_name', 'last_name']


class StudentSerializer(serializers.ModelSerializer):
    # classroom = serializers.RelatedField(source='classroom.class_name', read_only=True)
    class Meta:
        model = Student
        fields = ['id', 'name', 'phone_number', 'semester_average','classroom']


class AttendanceSerializer(serializers.ModelSerializer):
    students = StudentSerializer(many=True, read_only=True)
        
    class Meta:
        model = Attendance
        fields = ['daily_attendance', 'date', 'students']


class ClassroomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Classroom
        fields = ['id', 'class_name']


class StudClassSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField(source='classroom.id')
    classroom = serializers.ReadOnlyField(source='classroom.class_name')
    student = serializers.ReadOnlyField(source='student.name')

    class Meta:
        model = StudClass

        fields = ('id', 'classroom', 'student',)



class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['pk','title',]


class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = ['pk', 'title',]


class SubjectSerializer(WritableNestedModelSerializer):
    user_id = serializers.CharField(default=1)

    lists = ListSerializer(many=True)

    class Meta:
        model = Subject
        fields = ['pk','user_id','title', 'lists',]
    
