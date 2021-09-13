from django.db import models

class User(models.Model):
    name = models.CharField("Name", max_length=100)
    email = models.EmailField()
    city = models.CharField("City", max_length=30, null=True)
    state = models.CharField("State", max_length=30, null=True)
    zip = models.IntegerField("Zip", null=True)
    balance = models.DecimalField(
        default=1000, decimal_places=2, max_digits=30, blank=True)
    

    def __str__(self):
        return self.name