from django.contrib.auth import get_user_model, models
from rest_framework import serializers
from rest_framework.generics import get_object_or_404

from .utils import get_firebase_token, get_firebase_token_refresh

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class TokenObtainSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255, required=True, write_only=True)
    password = serializers.CharField(max_length=255, required=True, write_only=True)
    idToken = serializers.CharField(read_only=True)
    refreshToken = serializers.CharField(read_only=True)

    def validate(self, attrs):
        username = attrs.pop('username')
        password = attrs.pop('password')
        user = get_object_or_404(User, username=username)
        if not user.check_password(raw_password=password):
            raise serializers.ValidationError({'message': 'Incorrect password.'})
        id_token, refresh_token = get_firebase_token(username)
        attrs['idToken'] = id_token
        attrs['refreshToken'] = refresh_token
        return attrs


class TokenRefreshSerializer(serializers.Serializer):
    idToken = serializers.CharField(read_only=True)
    refreshToken = serializers.CharField()

    def validate(self, attrs):
        refresh_token = attrs.pop('refreshToken')
        id_token, refresh_token = get_firebase_token_refresh(refresh_token)
        if not id_token or not refresh_token:
            raise serializers.ValidationError({'message': 'Invalid refresh token'})
        attrs['idToken'] = id_token
        attrs['refreshToken'] = refresh_token
        return attrs
