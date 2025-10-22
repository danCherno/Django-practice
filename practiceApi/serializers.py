from rest_framework import serializers

from practiceApi import models

class HelloSerializer(serializers.Serializer):
    """ Serializes a name field for testing our APIView """
    name = serializers.CharField(max_length=10)

class UserProfileSerializer(serializers.ModelSerializer):
    """ Serializes a user profile object """

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        user = models.UserProfile.objects.create_User(
            email = validated_data['email'],
            password = validated_data['password'],
        )

        return user

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
        
        return super.update(instance, validated_data)