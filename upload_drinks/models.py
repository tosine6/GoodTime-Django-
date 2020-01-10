from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class UploadDrink(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    quantity = models.IntegerField
    manufacturer = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField()