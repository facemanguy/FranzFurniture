from django.contrib import admin
from .models import FurnitureType, Furniture, FurnitureDetails

# Register your models here.
admin.site.register(FurnitureType)
admin.site.register(Furniture)
admin.site.register(FurnitureDetails)