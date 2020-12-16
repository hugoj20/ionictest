from users.models import User, Address
from users.serializers import UserSerializer, AddressSerializer
from rest_framework import generics
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from .utils import Util
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.core.exceptions import ObjectDoesNotExist
import json



class UserList(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def perform_create(self, serializer):
        instance = serializer.save()

        current_site = get_current_site(self.request).domain
        #relative_link = reverse('email_verify', kwargs={'token':instance.token,'pk':})

        absolute_url = 'http://example.domain.com/verify/email/'+ instance.token
        email_body = 'Hi ' + instance.name + ' use the link below to verify your email ' +absolute_url
        data = {
            'domain':absolute_url,
            'email_subject': 'Verify Your Email',
            'email_body': email_body,
            'email_reciver': instance.email,
        }
        Util.send_email(data)

class VerifyEmail(generics.UpdateAPIView):
    serializer_class = UserSerializer
    http_method_names = ['patch']
    def patch(self, request, token):
        decoded_token = json.loads(Util.cryptograpy_text(token, False))
        try:
            user = User.objects.get(username=decoded_token['username'])
        except ObjectDoesNotExist:
            return Response('invalid token', status=status.HTTP_400_BAD_REQUEST)
        
        data = {'status':'active'}
        serializer = UserSerializer(user, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class AddressList(generics.ListCreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

class AddressDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


