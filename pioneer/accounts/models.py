from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length =100, default='')
    phone = models.IntegerField(blank=True)
    image = models.ImageField(upload_to='image_profile', blank=True)

    def __str__(self):
        return self.user.username
