from django.contrib.auth import get_user_model
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'email', 'password', 'location')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = get_user_model().objects.create_user(
            password=validated_data['password'],
            email=validated_data['email'],
            location=validated_data['location'],
        )
        return user
