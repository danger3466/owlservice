from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

from django.contrib.auth.validators import UnicodeUsernameValidator


class User(AbstractUser):
    username_validator = UnicodeUsernameValidator()
    id = models.AutoField(db_column='user_id', primary_key=True)
    user_id_parent_id = models.PositiveIntegerField(blank=True, null=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    user_fullname = models.CharField(max_length=128, blank=True, null=True)
    user_company = models.CharField(max_length=48, blank=True, null=True)
    user_company_address = models.CharField(max_length=128, blank=True, null=True)
    user_company_tel = models.CharField(max_length=32, blank=True, null=True)
    user_company_logo = models.CharField(max_length=256, blank=True, null=True)
    username = models.CharField(
        db_column='user_name',
        max_length=150,
        unique=True,
        validators=[username_validator],
    )
    email = models.EmailField(db_column="user_email", blank=True)
    password = models.CharField(db_column="user_password", max_length=128, blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    date_joined = models.DateTimeField(default=timezone.now)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'users'
