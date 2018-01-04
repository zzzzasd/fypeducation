from rest_framework import serializers
from .models import User
from . models import Subject


class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('identity_number', 'password')
        write_only_fields = ('password',)

class SignInSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('identity_number', 'password')
        write_only_fields = ('password',)


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ('title')


class UserSerializer(serializers.ModelSerializer):
    subjects = SubjectSerializer(many=True)

    class Meta:
        model = User
        fields = ('identity_number', 'first_name', 'last_name', 'subjects')
