from rest_framework import serializers
from .models import User
from restaurant.serializers import RestaurantSerializer

class BaseUserSerializer(serializers.ModelSerializer):
    '''
    Base User serializer used as skeleton.
    '''
    class Meta:
        model = User
        fields = [ 'first_name', 'last_name', 'email', 'city', 'state', 'zip_code', 'balance']


class UserSerializer(BaseUserSerializer):
    '''
    User serializer for basic CRUD operations.
    '''
    class Meta(BaseUserSerializer.Meta):
        fields = ['id', 'password'] + BaseUserSerializer.Meta.fields
        extra_kwargs = {
            'password': {"write_only": True},
            'balance': {"read_only": True}
        }
        
    
class UserDetailSerializer(BaseUserSerializer):
    '''
    User serializer for basic CRUD operations without ID
    '''
    restaurants = RestaurantSerializer(read_only=True, many=True)
    class Meta(BaseUserSerializer.Meta):
        fields = BaseUserSerializer.Meta.fields + ['restaurants']
        extra_kwargs = {
            'balance': {"read_only": True}
        }
