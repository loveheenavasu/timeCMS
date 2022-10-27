from pyexpat import model
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser, PermissionsMixin, AbstractUser, )
from django.db import models
from django.contrib.auth.models import User


# class UserManager(BaseUserManager):
#     def _create_user(self, email: str, password: str = None, **kwargs):
#         if not email:
#             raise ValueError('Users must have an email address')
#         user = self.model(
#             email=self.normalize_email(email),
#             **kwargs
#         )
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
#     def create_user(self, email: str = None, password=None, **kwargs):
#         kwargs.setdefault('is_superuser', False)
#         return self._create_user(email=email, password=password, **kwargs)
#
#     def create_superuser(self, email, password, **kwargs):
#         kwargs.setdefault('is_superuser', True)
#         if kwargs.get('is_superuser') is not True:
#             raise ValueError('Superuser must have is_superuser=True.')
#         if password is None:
#             raise TypeError('Superusers must have a password.')
#         user = self._create_user(email=email, password=password, **kwargs)
#         user.is_superuser = True
#         user.is_staff = True
#         user.save()
#         return user
#

class Permission(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class Roles(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    permission = models.ForeignKey(Permission, null=True, blank=True, on_delete=models.CASCADE)
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_user = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class Address(models.Model):
    street = models.CharField(max_length=1000, null=True, blank=True)
    address = models.CharField(max_length=1000, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=1000, null=True, blank=True)
    zipcode = models.CharField(max_length=1000, null=True, blank=True)


class Users(AbstractUser):
    fullname = models.CharField(max_length=255, null=True, blank=True)
    username = models.CharField(max_length=255, null=True, blank=True, unique=True, error_messages={'unique': "A user with this username already exists.", })
    password = models.CharField(max_length=255)
    email = models.EmailField('email address', max_length=255, unique=True, error_messages={'unique': "A user with this email already exists.", })
    contact = models.BigIntegerField(null=True, blank=True)
    designation = models.CharField(max_length=255, null=True, blank=True)
    image = models.CharField(max_length=255, null=True, blank=True)
    education = models.CharField(max_length=255, null=True, blank=True)
    experience = models.CharField(max_length=255, null=True, blank=True)
    roles = models.ForeignKey(Roles, null=True, blank=True, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, null=True, blank=True, on_delete=models.CASCADE)
    description = models.TextField(max_length=500, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    # is_superuser = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta(AbstractUser.Meta):
        swappable = "settings.AUTH_USER_MODEL"
