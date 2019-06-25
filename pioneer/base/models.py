from django.db import models
from django.contrib.auth.models import User

class student(models.Model):
    name = models.CharField(max_length=50)
    emailid = models.EmailField(max_length=50)
    city = models.CharField(max_length=50, blank=True, null = True)
    marks = models.IntegerField(default = 0, blank =True, null = True)
    dat = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.name
        