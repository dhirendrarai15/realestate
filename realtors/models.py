from django.db import models
from datetime import datetime

# Create your models here.


class Realtor(models.Model):
    name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='photo/%Y/%m/%d/')
    description = models.TextField(blank=True)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    topseller = models.BooleanField(default=False)
    datehired = models.DateTimeField(default=datetime.now,blank=True)

    def __str__(self):
        return self.name