from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields = ['id', 'name' ,'roll']

    # def validate_roll(self,value):
    #     if value>=200:
    #         raise serializers.ValidationError('Seat Full')