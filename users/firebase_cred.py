import firebase_admin
from firebase_admin import credentials
from django.conf import settings


def get_credentials():
    cred = credentials.Certificate(settings.FIREBASE_CONFIG)
    return firebase_admin.initialize_app(cred)
