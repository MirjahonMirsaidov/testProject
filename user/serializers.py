from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate

from user.utils import send_email_verification


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('email', 'password')
        extra_kwargs = {
            'password': {'write_only': True, 'min_length': 5}
        }

    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)
        send_email_verification(user)
        return user


class UserSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    department = serializers.CharField(required=False)

    class Meta:
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name', 'department')

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user


class AuthTokenSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=True
    )

    def validate(self, attrs):
        """Validate and authenticate user"""
        email = attrs.get('email')
        password = attrs.get('password')
        user = authenticate(
            request=self.context.get('request'),
            username=email,
            password=password,
        )
        print(user)
        if not user:
            msg = 'Validated data is not available to authenticate. Make sure you confirm your email address.'
            raise serializers.ValidationError(msg, code='authentication')

        attrs['user'] = user
        return attrs


class EmailVerificationSerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length=555)

    class Meta:
        model = get_user_model()
        fields = ('token', )


class ChangePasswordSerializer(serializers.Serializer):
    password1 = serializers.CharField(max_length=255)
    password2 = serializers.CharField(max_length=255)


class UpdatePasswordSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255)