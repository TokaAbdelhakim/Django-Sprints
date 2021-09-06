from django.db import models
from django.urls import reverse

#category class
class Category (models.Model):
    name = models.CharField(max_length=255)
    def get_absolute_url(self):
        return reverse('all-products')

# Create your models here.
class Product (models.Model):
    name = models.CharField(max_length=20, null=False)
    description = models.TextField()
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    price = models.DecimalField(default=0, max_digits=6, decimal_places=2)
    category = models.CharField(max_length=20, null=False, default='Accessories')

    def get_absolute_url(self):
        return reverse('all-products')
    
