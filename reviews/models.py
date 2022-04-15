from itertools import product
from django.db import models

class Review(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    stars = models.IntegerField()
    recommend = models.CharField(max_length=255)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
