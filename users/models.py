from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

from referral.constants import LENGTH_PHONE_NUMBER, LENGTH_INVITE_CODE
from users.managers import CustomUserManager
from users.utils import generate_invite_code


class User(AbstractBaseUser):
    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ()
    password = None

    phone = models.CharField(
        verbose_name='Phone number',
        max_length=LENGTH_PHONE_NUMBER,
        unique=True
    )
    invite_code = models.CharField(
        verbose_name='Invite code',
        max_length=LENGTH_INVITE_CODE,
        default=generate_invite_code,
        unique=True
    )
    inviter = models.CharField(
        verbose_name='Inviter',
        max_length=LENGTH_INVITE_CODE,
        blank=True,
        null=True
    )
    invited = models.JSONField(
        verbose_name='Invited',
        default=list,
        blank=True
    )
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()
