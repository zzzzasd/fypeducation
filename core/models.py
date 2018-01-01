from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    identity_number = models.IntegerField(max_length=30, unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    is_claimed = models.BooleanField(default=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = 'identity_number'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()
    

class Subject(models.Model):
    author = models.ForeignKey('User', on_delete=models.PROTECT)
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class List(models.Model):
    subject = models.ForeignKey('core.Subject', on_delete=models.PROTECT)
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title