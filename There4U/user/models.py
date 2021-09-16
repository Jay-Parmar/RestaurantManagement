from django.db import models
from utils import check_positive
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser

from .managers import UserManager

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(help_text="Email ID of User", unique=True)
    first_name = models.CharField(max_length=30, help_text="First Name of User", blank=True)
    last_name = models.CharField(max_length=30, help_text="Last Name of User", blank=True)
    city = models.CharField(max_length=30, help_text="Current City of User")
    state = models.CharField(max_length=30, help_text="Current State of User")
    zip_code = models.PositiveIntegerField(help_text="Zip Code of User's Address")
    balance = models.DecimalField(default=1000, decimal_places=2, max_digits=30, validators=[check_positive])
    
    date_joined = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'city', 'state', 'zip_code']

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name
