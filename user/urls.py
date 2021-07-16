from django.urls import path
from django.contrib.auth import views as auth_views

from .views import UserApiView, CreateTokenView, UserUpdateView, EmailVerifyView, ChangePasswordView, UpdatePasswordview

app_name = 'user'

urlpatterns = [
    path('register/', UserApiView.as_view(), name='create'),
    path('login/', CreateTokenView.as_view(), name='token'),
    path('me/', UserUpdateView.as_view(), name='me'),
    path('password-reset/', auth_views.PasswordResetView.as_view(), name='password-reset'),
    path('email-verify/', EmailVerifyView.as_view(), name='email-verify'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('update-password/', UpdatePasswordview.as_view(), name='update-password'),
]