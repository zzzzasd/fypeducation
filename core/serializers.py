from rest_framework import serializers
from .models import User
from .models import Subject
from django.contrib.auth import get_user_model


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
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = get_user_model().objects.create(
            identity_number = validated_data['identity_number']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    class Meta:
        model = get_user_model()
        fields = ('identity_number', 'password', 'first_name', 'last_name', 'subjects')
