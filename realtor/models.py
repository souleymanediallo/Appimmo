from django.db import models

# Create your models here.
class Realtor(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="photo_realtor/%Y/")
    description = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name