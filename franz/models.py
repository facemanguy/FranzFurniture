from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class FurnitureType(models.Model):
    typeName=models.CharField(max_length=255)
    typeDescription=models.TextField(null=True, blank=True)

    def __str__(self):
        return self.typename

    class Meta:
        db_table='furnituretype'
        verbose_name_plural='furnituretypes'

class Furniture(models.Model):
    furnitureName=models.CharField(max_length=255)
    furnitureType=models.ForeignKey(FurnitureType, on_delete=models.DO_NOTHING)
    user=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    dateEntered=models.DateTimeField()
    furniturePrice=models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    furnitureDescription=models.TextField(null=True)

    def __str__(self):
        return self.furnitureName

    class Meta:
        db_table='furniture'

class FurnitureDetails(models.Model):
    detailName=models.CharField(max_length=255)
    product=models.ForeignKey(Furniture, on_delete=models.CASCADE)
    length=models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    width=models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    height=models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    materials=models.TextField(null=True, blank=True)

    def __str__(self):
        return self.detailName

    class Meta:
        db_table='details'