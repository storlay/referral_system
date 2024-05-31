from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

from referral.constants import LENGTH_PHONE_NUMBER, LENGTH_INVITE_CODE
from users.managers import CustomUserManager
from users.utils import generate_invite_code
from users.validators import phone_validator


class User(AbstractBaseUser):
    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ()

    phone = models.CharField(
        verbose_name='Phone number',
        max_length=LENGTH_PHONE_NUMBER,
        validators=(phone_validator,),
        unique=True
    )
    invite_code = models.CharField(
        verbose_name='Invite code',
        max_length=LENGTH_INVITE_CODE,
        default=generate_invite_code,
        unique=True
    )
    invited = models.JSONField(
        verbose_name='Invited',
        default=list
    )
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()