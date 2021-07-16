import jwt
from rest_framework import generics, authentication, permissions, status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.settings import api_settings

from testProject import settings
from .models import User
from .serializers import UserSerializer, AuthTokenSerializer, UserCreateSerializer, EmailVerificationSerializer, \
    ChangePasswordSerializer, UpdatePasswordSerializer
from .utils import send_change_password


class UserApiView(generics.CreateAPIView):
    serializer_class = UserCreateSerializer


class CreateTokenView(ObtainAuthToken):
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UserUpdateView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        return self.request.user


class EmailVerifyView(generics.GenericAPIView):
    serializer_class = EmailVerificationSerializer

    def get(self, request):
        token = request.GET.get('token')
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            user = User.objects.get(id=payload['user_id'])
            if not user.is_active:
                user.is_active = True
                user.save()
                return Response({'email': 'Successfully activated'}, status=status.HTTP_200_OK)
        except jwt.ExpiredSignatureError as identifier:
            return Response({'error': 'Activation Expired'}, status=status.HTTP_400_BAD_REQUEST)
        except jwt.exceptions.DecodeError as identifier:
            return Response({'error': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)


class UpdatePasswordview(generics.GenericAPIView):
    serializer_class = UpdatePasswordSerializer

    def post(self, request):
        email = request.data.get('email')
        try:
            user = User.objects.get(email=email)
            send_change_password(user)
            return Response({'password': 'Change password link send to your email address'}, status=status.HTTP_200_OK)
        except:
            return Response({'error': 'This email does not exist'}, status=status.HTTP_400_BAD_REQUEST)


class ChangePasswordView(generics.GenericAPIView):
    serializer_class = ChangePasswordSerializer

    def post(self, request):
        token = request.GET.get('token')
        password1 = request.data.get('password1')
        password2 = request.data.get('password2')
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            user = User.objects.get(id=payload['user_id'])
            print(password1 == password2)
            if password1 == password2:
                user.set_password(password1)
                user.save()
                print('done')
                return Response({'password': 'Password successfully changed'}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Passwords does not match!'}, status=status.HTTP_400_BAD_REQUEST)
        except jwt.ExpiredSignatureError as identifier:
            return Response({'error': 'Activation Expired'}, status=status.HTTP_400_BAD_REQUEST)
        except jwt.exceptions.DecodeError as identifier:
            return Response({'error': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)
