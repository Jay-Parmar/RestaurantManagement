from datetime import datetime
from django.db import models
from utils import check_positive
from django.contrib.auth.models import User
from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser

from .managers import UserManager

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(help_text="Email ID of User", unique=True)
    password = models.CharField(max_length=50, help_text="Password length cannot be more than 50")
    first_name = models.CharField(max_length=30, help_text="First Name of User", blank=True)
    last_name = models.CharField(max_length=30, help_text="Last Name of User", blank=True)
    city = models.CharField(max_length=30, help_text="Current City of User")
    state = models.CharField(max_length=30, help_text="Current State of User")
    zip_code = models.PositiveIntegerField(help_text="Zip Code of User's Address")
    balance = models.DecimalField(default=1000, decimal_places=2, max_digits=30, validators=[check_positive])
    
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['fname', 'city', 'state', 'zip_code']

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

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)


# class User(models.Model):
#     '''
#     Model for User using the API.
#     '''
#     name = models.CharField(max_length=100, help_text="Full Name of User")
#     email = models.EmailField(help_text="Email ID of User", unique=True)
#     city = models.CharField(max_length=30, help_text="Current City of User")
#     state = models.CharField(max_length=30, help_text="Current State of User")
#     zip_code = models.PositiveIntegerField(help_text="Zip Code of User's Address")
#     balance = models.DecimalField(default=1000, decimal_places=2, max_digits=30, validators=[check_positive])
    
#     def __str__(self):
#         return self.name
