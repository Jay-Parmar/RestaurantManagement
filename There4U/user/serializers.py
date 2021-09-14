from rest_framework import serializers
from .models import User
from restaurant.serializers import RestaurantSerializer

class UserSerializer(serializers.ModelSerializer):
    '''
    User serializer for basic CRUD operations.
    '''
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'city', 'state', 'zip_code', 'balance']
        
    
class UserSerializerWithoutID(serializers.ModelSerializer):
    '''
    User serializer for basic CRUD operations without ID
    '''
    restaurants = RestaurantSerializer(read_only=True, many=True)
    class Meta:
        model = User
        fields = ['name', 'email', 'city', 'state', 'zip_code', 'balance', 'restaurants']
