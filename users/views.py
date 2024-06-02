import time

from django.contrib.auth import get_user_model, authenticate, login
from rest_framework import status
from rest_framework.generics import RetrieveAPIView, GenericAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from users.serializers import UserAuthSerializer, UserDetailSerializer, UserWriteCodeSerializer, \
    UserAuthConfirmSerializer
from users.utils import generate_auth_code

User = get_user_model()


class UserAuthAPIView(GenericAPIView):
    serializer_class = UserAuthSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            phone_number = serializer.data.get('phone_number')
            try:
                User.objects.get(phone=phone_number)
            except User.DoesNotExist:
                User.objects.create(phone=phone_number)

            auth_code = generate_auth_code()

            # Simulating sending a code
            time.sleep(2)

            request.session['auth_code'] = auth_code
            request.session['phone_number'] = phone_number
            return Response(
                {
                    'message': 'Code sent successfully',
                    'phone_number': phone_number
                },
                status=status.HTTP_200_OK
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class UserConfirmPhoneAPIView(GenericAPIView):
    serializer_class = UserAuthConfirmSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            entered_code = serializer.data.get('code')
            auth_code = request.session.get('auth_code')
            phone_number = request.session.get('phone_number')

            if entered_code == auth_code:
                user = authenticate(request, phone=phone_number)
                if user is not None:
                    user.is_active = True
                    user.save()
                    login(request, user)
                    user_data = UserDetailSerializer(user).data
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
        return Response(
            serializer.errors,
            status=status.HTTP_401_UNAUTHORIZED
        )


class UserDetailAPIView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer


class UserWriteCodeAPIView(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserWriteCodeSerializer
    partial = True

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(
            instance,
            data=request.data,
            partial=self.partial
        )

        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def get_object(self):
        return self.request.user
