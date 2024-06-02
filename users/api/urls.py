from django.urls import path

from users.api.views import UserAuthAPIView, UserConfirmPhoneAPIView, UserDetailAPIView, UserWriteCodeAPIView, \
    UserLogoutAPIView

urlpatterns = [
    path(
        'login/',
        UserAuthAPIView.as_view(),
        name='login'
    ),
    path(
        'login/confirm/',
        UserConfirmPhoneAPIView.as_view(),
        name='login-confirm'
    ),
    path(
        'logout/',
        UserLogoutAPIView.as_view(),
        name='logout'
    ),
    path(
        '<int:pk>/',
        UserDetailAPIView.as_view(),
        name='detail'
    ),
    path(
        'add-inviter/',
        UserWriteCodeAPIView.as_view(),
        name='add-inviter'
    )
]
