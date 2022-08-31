import json

import requests
from django.conf import settings
from firebase_admin.auth import create_custom_token


def get_firebase_token(username):
    url = settings.FIREBASE_TOKEN_URL
    data = {
        "token": create_custom_token(uid=username),
        "returnSecureToken": True
    }
    response = requests.post(url=url, data=data)
    data = json.loads(response.text)
    return data.get('idToken'), data.get('refreshToken')


def get_firebase_token_refresh(refresh_token):
    url = settings.FIREBASE_TOKEN_REFRESH_URL
    data = {
        'grant_type': 'refresh_token',
        'refresh_token': refresh_token
    }
    response = requests.post(url=url, data=data)
    data = json.loads(response.text)
    return data.get('id_token'), data.get('refresh_token')
