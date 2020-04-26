from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=125)

class Toy(models.Model):
    name = models.CharField(max_length=125)
    imageURL = models.CharField(max_length=125)
    description = models.CharField(max_length=1250)
    price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)

class Order(models.Model):
    name = models.CharField(max_length=125)
    phone = models.CharField(max_length=125)
    toy = models.ForeignKey(Toy, on_delete=models.CASCADE, blank=True, null=True)
