from django.db import models
from utils import check_positive

class User(models.Model):
    '''
    Model for User using the API
    '''
    name = models.CharField(max_length=100, help_text="Full Name of User")
    email = models.EmailField(help_text="Email ID of User", unique=True)
    city = models.CharField(max_length=30, help_text="Current City of User")
    state = models.CharField(max_length=30, help_text="Current State of User")
    zip_code = models.PositiveIntegerField(help_text="Zip Code of User's Address", default=00000)
    balance = models.DecimalField(default=1000, decimal_places=2, max_digits=30, validators=[check_positive])
    
    def __str__(self):
        return self.name
