from django.db import models
from django.core.exceptions import ValidationError

def check_positive(value):
    '''
    Check if given value is positive or not. 
    If not, raises a validation error.
    '''
    if value < 0:
        raise ValidationError("Invalid Value Provided for this Field")
    else:
        return value

class User(models.Model):
    '''
    Model for User using the API
    '''
    name = models.CharField(max_length=100, 
        help_text="Enter Your Full Name"
        )
    email = models.EmailField(
        help_text="Enter Email ID"
        )
    city = models.CharField(max_length=30, 
        help_text="Enter your current city"
        )
    state = models.CharField(max_length=30, 
        help_text="Enter your current state"
        )
    zip = models.PositiveIntegerField(
        help_text="Enter Your Zip Code",
        validators=[check_positive]
        )
    balance = models.DecimalField(
        default=1000, decimal_places=2, max_digits=30,
        validators=[check_positive]
        )
    

    def __str__(self):
        return self.name
