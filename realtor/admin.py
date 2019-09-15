from django.contrib import admin
from .models import Realtor

# Register your models here.
@admin.register(Realtor)
class RealtorAdmin(admin.ModelAdmin):
    pass