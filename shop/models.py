from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    location = models.TextField(max_length=200)
    phone_number = models.BigIntegerField()
    age = models.IntegerField()
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    
    def __str__(self):
        return self.user

