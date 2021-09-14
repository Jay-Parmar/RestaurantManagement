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
