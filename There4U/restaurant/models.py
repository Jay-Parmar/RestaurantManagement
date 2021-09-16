from django.db import models
from django.db.models.fields.related import ForeignKey, ManyToManyField
from utils import check_positive
from user.models import User

class Restaurant(models.Model):
    '''
    Model for Restaurant consisting of restaurant delails
    '''
    name = models.CharField(max_length=100, help_text="Restaurant name")
    city = models.CharField(max_length=30, help_text="Restaurant city")
    owners = ManyToManyField(User, related_name='restaurants')

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    '''
    Model to List unique menu items for all restaurants
    '''
    restaurant = ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, help_text="Menu Item Name")
    price = models.DecimalField(
        decimal_places=2, max_digits=30, validators=[check_positive], help_text="Menu Item Price"
    )
    description = models.CharField(max_length=200, blank=True, help_text="Menu Item Description")
    quantity_available = models.PositiveIntegerField(help_text="Menu Item Quantity Available")

    def __str__(self):
        return self.name
