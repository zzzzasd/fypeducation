from django.contrib.auth.models import Group
from oauth2_provider.contrib.rest_framework import (TokenHasReadWriteScope,
                                                    TokenHasScope)
from rest_framework import permissions, viewsets

from .models import User, Subject, Classroom, Student, Attendance
from .serializers import GroupSerializer, UserSerializer, ClassroomSerializer, StudentSerializer, AttendanceSerializer, SubjectSerializer


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    #permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    #permission_classes = [permissions.IsAuthenticated, TokenHasScope]
    #required_scopes = ['groups']
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class ClassroomViewSet(viewsets.ModelViewSet):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer


class SubjectViewSet(viewsets.ModelViewSet):
    # permission_classes = [permissions.IsAuthenticated, TokenHasScope]
    # required_scopes = ['groups']
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer



