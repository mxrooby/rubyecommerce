from django.db import models

# Product Model
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    category = models.CharField(max_length=50)
    tags = models.JSONField(default=list)  # Store tags as a list of strings (requires Django 3.1+)

    def __str__(self):
        return self.name
