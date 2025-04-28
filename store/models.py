from djongo import models  # Use djongo, not django.db.models

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    category = models.CharField(max_length=50)
    tags = models.JSONField(default=list)  # Optional: for AI tag suggestions

    def __str__(self):
        return self.name
