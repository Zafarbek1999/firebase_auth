from django.urls import path, include
from rest_framework.routers import DefaultRouter

from users.views import UserViewSet, TokenObtainView, TokenRefreshView

router = DefaultRouter()
router.register('users', UserViewSet)

urlpatterns = [
    path('users/', include(router.urls)),
    path('token/', TokenObtainView.as_view(), name='token_obtain'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
]
