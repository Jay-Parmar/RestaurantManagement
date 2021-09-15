from django.db import models
from user.models import User
from restaurant.models import Restaurant, MenuItem
from utils import check_positive


class Order(models.Model):
    '''
    Model to store individual orders.
    '''
    ORDER_CHOICES = (
        ("PLACED", "Placed"),
        ("ACCEPTED", "Accepted"),
        ("REJECTED", "Rejected"),
        ("DISPATCHED", "Dispatched"),
        ("CANCELLED", "Cancelled"),
        ("DELIVERED", "Delivered"),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    total_bill = models.DecimalField(decimal_places=2, max_digits=30, validators=[check_positive],
                                     help_text="Total bill including all the items")
    date_time = models.DateTimeField(auto_now_add=True, help_text="Date and Time of the order")
    status = models.CharField(max_length=20, choices=ORDER_CHOICES, default="PLACED",
                              help_text="Current Status of Order")

    def __str__(self):
        return self.name


class OrderItem(models.Model):
    '''
    Model to store items in every order.
    '''
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.DO_NOTHING)
    price = models.DecimalField(decimal_places=2, max_digits=30, validators=[check_positive],
                                help_text="Price of single Item")
    quantity = models.PositiveIntegerField(help_text="Quantity of given item ordered")

    def __str__(self):
        return self.name
