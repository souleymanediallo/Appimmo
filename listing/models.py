from django.db import models
from realtor.models import Realtor

# Create your models here.
class Listing(models.Model):
    realtor = models.ForeignKey(Realtor, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    garage = models.IntegerField(default=0)
    sqft = models.IntegerField()
    lot_size = models.DecimalField(max_digits=5, decimal_places=1)
    photo_main = models.ImageField(upload_to='photos/%Y/')
    photo_1 = models.ImageField(upload_to='photos/%Y/', blank=True, null=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/', blank=True, null=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/', blank=True, null=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/', blank=True, null=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/', blank=True, null=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title