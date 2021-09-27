from django.db import models
from django.utils.timezone import now
from realtors.models import Realtor

# Create your models here.
class Listing(models.Model):

    class SaleType(models.TextChoices):
        FOR_SALE = 'for_sale'
        For_RENT = 'for_rent'

    class HomeType(models.TextChoices):
        HOUSE = 'house'
        CONDO = 'condo'
        TOWNHOUSE = 'townhouse'

    realtor = models.ForeignKey(Realtor,on_delete=models.DO_NOTHING)
    slug = models.CharField(max_length=200,unique=True)
    title = models.CharField(max_length=150)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=10)
    description = models.TextField(blank=True)
    saletype = models.CharField(max_length=50,choices=SaleType.choices,default=SaleType.FOR_SALE)
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=2,decimal_places=1)
    hometype = models.CharField(max_length=50,choices=HomeType.choices,default=HomeType.HOUSE)
    sqft = models.IntegerField()
    openhouse = models.BooleanField(default=False)
    photomain = models.ImageField(upload_to='photos/%y/%m/%d')
    photo1 = models.ImageField(upload_to='photos/%y/%m/%d',blank=True)
    photo1 = models.ImageField(upload_to='photos/%y/%m/%d',blank=True)
    photo2 = models.ImageField(upload_to='photos/%y/%m/%d',blank=True)
    photo3 = models.ImageField(upload_to='photos/%y/%m/%d',blank=True)
    photo4 = models.ImageField(upload_to='photos/%y/%m/%d',blank=True)
    photo5 = models.ImageField(upload_to='photos/%y/%m/%d',blank=True)
    photo6 = models.ImageField(upload_to='photos/%y/%m/%d',blank=True)
    photo7 = models.ImageField(upload_to='photos/%y/%m/%d',blank=True)
    photo8 = models.ImageField(upload_to='photos/%y/%m/%d',blank=True)
    photo9 = models.ImageField(upload_to='photos/%y/%m/%d',blank=True)
    photo10 = models.ImageField(upload_to='photos/%y/%m/%d',blank=True)
    photo11 = models.ImageField(upload_to='photos/%y/%m/%d',blank=True)
    photo12 = models.ImageField(upload_to='photos/%y/%m/%d',blank=True)
    photo13 = models.ImageField(upload_to='photos/%y/%m/%d',blank=True)
    photo14 = models.ImageField(upload_to='photos/%y/%m/%d',blank=True)
    photo15 = models.ImageField(upload_to='photos/%y/%m/%d',blank=True)
    photo16 = models.ImageField(upload_to='photos/%y/%m/%d',blank=True)
    photo17 = models.ImageField(upload_to='photos/%y/%m/%d',blank=True)
    photo18 = models.ImageField(upload_to='photos/%y/%m/%d',blank=True)
    photo19= models.ImageField(upload_to='photos/%y/%m/%d',blank=True)
    photo20= models.ImageField(upload_to='photos/%y/%m/%d',blank=True)
    ispublished = models.BooleanField(default=True)
    listdate = models.DateTimeField(default=now,blank=True)

    def __str__(self):
        return self.title