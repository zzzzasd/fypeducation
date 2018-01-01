from rest_framework import serializers
from core.models import User

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    identity_number = serializers.IntegerField(required=True, unique=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data)
    instance.identity_number = validated_data.get('title', instance.title)
    instance.first_name = validated_data.get('first_name', instance.first_name)
    instance.last_name = validated_data.get('last_name', instance.last_name)
    instance.save()
    return instance