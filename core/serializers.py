from django.contrib.auth.models import Group
from rest_framework import serializers

from .models import User, Subject, List, Task
from drf_writable_nested import WritableNestedModelSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['identity_number', 'first_name', 'last_name']


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
    
