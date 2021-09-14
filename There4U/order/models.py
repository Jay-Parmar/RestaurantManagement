from django.db import models
from user.models import User
from restaurant.models import Restaurant, MenuItem
from utils import check_positive

class Order(models.Model):
    '''
    Model to store individual orders
    '''
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant_id = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    total_bill = models.DecimalField(decimal_places=2, max_digits=30, validators=[check_positive], 
        help_text="Total bill including all the items")
    date_time = models.DateTimeField(auto_now_add=True, help_text="Date and Time of the order")
    status = models.CharField(max_length=20, default="Placed", help_text="Current Status of Order")

class OrderItem(models.Model):
    '''
    Model to store items in every order
    '''
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    food_id = models.ForeignKey(MenuItem, on_delete=models.DO_NOTHING)
    price = models.DecimalField(decimal_places=2, max_digits=30, validators=[check_positive], 
        help_text="Price of single Item")
    quantity = models.PositiveIntegerField(help_text="Quantity of given item ordered")
