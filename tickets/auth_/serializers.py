from rest_framework import serializers
from .models import MainUser, Profile


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainUser
        fields = ('email', 'password')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        user = MainUser.objects.create_user(email=validated_data['email'], password=validated_data['password'])
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainUser
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        exclude = ('user',)

    def create(self, validated_data):
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        bio = validated_data['bio']
        birth_date = validated_data['birth_date']
        photo = validated_data['photo']
        user = self.context.get('user')

        profile = Profile.objects.create(first_name=first_name, last_name=last_name, bio=bio, birth_date=birth_date,
                                         photo=photo, user=user)
        return profile
