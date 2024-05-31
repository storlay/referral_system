from django.urls import path

from users.views import UserAuthAPIView, UserConfirmPhoneAPIView

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
    )
]
