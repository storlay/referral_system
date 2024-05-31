import time

from django.contrib.auth import get_user_model, authenticate, login
from rest_framework import status
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from users.serializers import UserAuthSerializer, UserDetailSerializer
from users.utils import generate_auth_code

User = get_user_model()


class UserAuthAPIView(APIView):

    def post(self, request):
        phone_number = request.data.get('phone_number')

        try:
            user = User.objects.get(phone=phone_number)
        except User.DoesNotExist:
            user = User.objects.create(phone=phone_number)

        user_data = UserAuthSerializer(user).data
        auth_code = generate_auth_code()

        time.sleep(2)

        request.session['auth_code'] = auth_code
        request.session['phone_number'] = phone_number
        return Response(
            {
                'message': 'Code sent successfully',
                'user': user_data
            },
            status=status.HTTP_200_OK
        )


class UserConfirmPhoneAPIView(APIView):

    def post(self, request):
        entered_code = request.data.get('code')
        auth_code = request.session.get('auth_code')
        phone_number = request.session.get('phone_number')

        if entered_code == auth_code:
            user = authenticate(request, phone=phone_number)
            if user is not None:
                user.is_active = True
                user.save()
                login(request, user)

                user_data = UserAuthSerializer(user).data
                return Response(
                    {
                        'message': 'Authentication successful',
                        'user': user_data
                    },
                    status=status.HTTP_200_OK
                )
            return Response(
                {'message': 'Authentication failed'},
                status=status.HTTP_401_UNAUTHORIZED)
        return Response(
            {'message': 'Invalid code'},
            status=status.HTTP_401_UNAUTHORIZED
        )


class UserDetailAPIView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
