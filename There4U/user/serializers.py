from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    '''
    User serializer for basic CRUD operations.
    '''
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'city', 'state', 'zip', 'balance']
