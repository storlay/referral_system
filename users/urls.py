from django.urls import path, include

from users.views import AuthenticationView, ConfirmPhoneView

urlpatterns = [
    path('login/', AuthenticationView.as_view(), name='login'),
    path('login/confirm/', ConfirmPhoneView.as_view(), name='login-confirm')
]
