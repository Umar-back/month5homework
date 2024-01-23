import random
from django.contrib import admin
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework.authtoken.models import Token  # Import from the correct location
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import Confirm
from users.serializers import RegisterSerializer, LoginSerializer, ConfirmSerializer


# @api_view(['POST'])
# def register(request):
#     serializer = RegisterSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     user = User.objects.create_user(**serializer.validated_data, is_active=False)
#     confirmation = Confirm.objects.create(user=user, code=random.randint(100000, 999999))
#     return Response({'code': confirmation.code}, status=201)

class RegisterAPIview(APIView):
    serializer_class = RegisterSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = User.objects.create_user(**serializer.validated_data, is_active=False)
        confirmation = Confirm.objects.create(user=user, code=random.randint(100000, 999999))
        return Response({'code': confirmation.code}, status=201)


#
# @api_view(['POST'])
# def confirm(request):
#     serializer = ConfirmSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     code = serializer.validated_data.get('code', None)
#     confirmation = get_object_or_404(Confirm, code=code)
#     user = confirmation.user
#     user.is_active = True
#     user.save()
#     return Response({'status': 'success'}, status=200)

class ConfirmAPIview(APIView):
    serializer_class = ConfirmSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        code = serializer.validated_data.get('code', None)
        confirmation = get_object_or_404(Confirm, code=code)
        user = confirmation.user
        user.is_active = True
        user.save()
        return R





# @api_view(['POST'])
# def login_view(request):
#     serializer = LoginSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     user = authenticate(request, **serializer.validated_data)
#
#     if user:
#         login(request, user)
#         token, created = Token.objects.get_or_create(user=user)
#         return Response({'token': token.key})
#
#     return Response({'error': 'Invalid login'}, status=400)


class LoginAPIview(APIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(request, **serializer.validated_data)

        if user:
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})

        return Response({'error': 'Invalid login'}, status=400)
