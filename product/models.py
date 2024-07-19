from django.db import models
from django.db.models.manager import Manager
from autoslug import AutoSlugField
class Product(models.Model):
    objects = Manager()
    title = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    image = models.ImageField(upload_to='products/')

    product_slug = AutoSlugField(populate_from ="title",unique= True, null=True,default=None)

   