from rest_framework import serializers
from .models import User, Profile

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'role', 'password', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'update_at']
        
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
    
    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password:
            instance.set_password(password)  
        instance.save()
        return instance

from rest_framework import serializers


class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    user = serializers.ReadOnlyField(source='user.email')
    role = serializers.ReadOnlyField(source='user.role')

    class Meta:
        model = Profile
        fields = ['id', 'username', 'user', 'role', 'date_of_birth', 'address', 'phone_number']  
        read_only_fields = ['user'] 

    def create(self, validated_data):
        profile = Profile(**validated_data)
        profile.save()  
        return profile

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()  
        return instance
