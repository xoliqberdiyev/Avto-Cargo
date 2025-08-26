from django.db import models
from django.contrib.auth.models import AbstractUser

from core.apps.common.models import BaseModel
from core.apps.accounts.manager import UserManager


class User(AbstractUser, BaseModel):
    full_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    passport_id = models.CharField(max_length=20, null=True)
    pnfl = models.CharField(max_length=20, null=True)

    first_name = None
    last_name = None
    username = None
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email 
    
    class Meta:
        verbose_name = 'foydalanuvchi'
        verbose_name_plural = 'foydalanuvchilar'