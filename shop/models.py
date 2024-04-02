from django.db import models

# Create your models here.


class Products(models.Model):
    product_title = models.CharField(max_length=200)
    product_price = models.FloatField()
    product_discount_price = models.FloatField()
    product_category = models.CharField(max_length=200)
    product_description = models.TextField()
    # to store image url
    product_image = models.CharField(max_length=300)

    def __str__(self):
        return self.product_title


class Order(models.Model):
    items = models.CharField(max_length=1000)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    address = models.CharField(max_length=1000)
    city = models.CharField(max_length=200)
    state  = models.CharField(max_length=200)
    zip = models.CharField(max_length=200)
    totalcost = models.CharField(max_length=200,default="0")

