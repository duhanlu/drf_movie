from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User

from account.models import Profile


class CustomUniqueValidator(UniqueValidator):
    def __call__(self, value, serializer_field):
        self.message = 'Email already exist'
        return super().__call__(value, serializer_field)
        

class CustomUserCreateSerializer(UserCreateSerializer):
    email = serializers.EmailField(
        validators = [CustomUniqueValidator(queryset=User.objects.all())]
    )
    
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        
    def create(self, validated_data):
        user = UserCreateSerializer.create(self, validated_data)
        # write into profile model
        profile = Profile(user=user)
        profile.save()
            
        return user

class ProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Profile
        fields = "__all__"   
class CustomUserSerializer(UserSerializer):
    profile = ProfileSerializer(read_only=True)
    
    class Meta(UserSerializer.Meta):
        fields = (*UserSerializer.Meta.fields , 'profile')
    
    
        
    