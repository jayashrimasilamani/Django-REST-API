from rest_framework import serializers

from profiles_api import models


class HelloSerializer(serializers.Serializer):
    """serializes the name field for apiview"""
    name = serializers.CharField(max_length=10)

class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""

    class Meta:
        model = models.UserProfile
        fields = ('id','email','name','password')
        extra_kwargs = {
            'password':{
                'write_only':True,
                'style':{'input_type':'password'}
            }
        }

    def create(self,validatd_data):
        """Create and return new user"""
        user = models.UserProfile.objects.create_user(
            email=validatd_data['email'],
            name=validatd_data['name'],
            password=validatd_data['password']

        )
        return user

    def update(self, instance, validated_data):
        """Handle updating user account"""

        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)
