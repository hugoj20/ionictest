from rest_framework import serializers 
from users.models import User, Address
from django.contrib.auth.hashers import make_password
from rest_framework.exceptions import NotFound, ValidationError
from .utils import Util
from rest_framework import status
import json 


import secrets

 
 
class UserSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = User
        fields = (
            'user_id',
            'name',
            'lastname',
            'username',
            'email',
            'status'
        )
        wrapper_name = 'users'
        extra_kwargs = {
            'password': {'write_only': True, 'min_length': 8},
            'token  ': {'write_only': True},
            'status  ': {'read_only': True},
            }

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        try:
            token = Util.cryptograpy_text(json.dumps({
                'email': validated_data['email'],
                'username': validated_data['username'],
            }))
        except:
            ValidationError('invalid Token', status=status.HTTP_400_BAD_REQUEST)
        validated_data['token'] = token

        return super(UserSerializer, self).create(validated_data)



        
class AddressSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Address
        fields = (
            'address_id',
            'owner_id',
            'owner_type',
            'property_type',
            'property_id',
            'city',
            'state',
            'street',
            'postal_code',
            'extra_info',
        )

        wrapper_name = 'address'


    def create(self, validated_data):
        try:
            User.objects.get(user_id = validated_data['owner_id'])
        except:
            raise NotFound("User not found")
        return super(AddressSerializer, self).create(validated_data)


