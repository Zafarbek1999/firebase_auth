from django.contrib.auth import get_user_model
from django.utils import timezone
from firebase_admin import auth
from rest_framework import authentication

from .exceptions import FirebaseError
from .exceptions import InvalidAuthToken
from .firebase_cred import get_credentials

default_app = get_credentials()


User = get_user_model()


class FirebaseAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.META.get("HTTP_AUTHORIZATION")
        if auth_header is None:
            return None
        id_token = auth_header.split(" ").pop()
        try:
            decoded_token = auth.verify_id_token(id_token)
        except Exception:
            raise InvalidAuthToken("Invalid auth token")
        if not id_token or not decoded_token:
            return None

        try:
            uid = decoded_token.get("uid")
        except Exception:
            raise FirebaseError()
        user, created = User.objects.get_or_create(username=uid)
        user.profile.last_activity = timezone.localtime()
        return user, None
