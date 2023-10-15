from django.contrib.auth import authenticate
from django.shortcuts import render
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from users.serializers import UserSerializer, LoginSerializer


class RegisterApiView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)
        else:
            data = {
                'message': 'Forms is not valid!'
            }
            return Response(data)







# class LoginApiView(APIView):
#     def post(self, request):
#         serializer = LoginSerializer(data=request.data)
#
#         if serializer.is_valid():
#             username = serializer.data['username']
#             password = serializer.data['password']
#
#             user = authenticate(username=username, password=password)
#
#             if user is None:
#                 data = {
#                     'status': status.HTTP_400_BAD_REQUEST,
#                     'message': "Bunday foydalanuvchi topilmadi"
#                 }
#                 return Response(data)
#
#             refresh = RefreshToken.for_user(user)
#
#             data = {
#                 'refresh': str(refresh),
#                 'access': str(refresh.access_token),
#             }
#
#             return Response(data)


# class LoginApiView(APIView):
#     def post(self, request):
#         serializer = LoginSerializer(data=request.data)
#
#         if serializer.is_valid():
#             user = serializer.validated_data['user']
#
#             data = {
#                 "success": True,
#                 "message": "You have successfully logged in"
#             }
#             return Response(data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



























