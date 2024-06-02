from django.contrib.auth import get_user_model
from rest_framework import serializers

from users.validators import confirm_code_validator, phone_validator

User = get_user_model()


class UserAuthSerializer(serializers.Serializer):
    phone_number = serializers.CharField(validators=(phone_validator,))


class UserAuthConfirmSerializer(serializers.Serializer):
    code = serializers.CharField(validators=(confirm_code_validator,))


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'phone', 'inviter', 'invite_code', 'invited')


class UserWriteCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('inviter',)

    def update(self, instance, validated_data):
        inviter_code = validated_data.pop('inviter')

        if instance.inviter:
            raise serializers.ValidationError(
                'The referral code can be entered only 1 time'
            )

        try:
            inviter = User.objects.get(invite_code=inviter_code)
            instance.inviter = inviter_code
            inviter.invited.append(instance.phone)
            inviter.save()
        except User.DoesNotExist:
            serializers.ValidationError('Incorrect invite code')

        return super().update(instance, validated_data)
