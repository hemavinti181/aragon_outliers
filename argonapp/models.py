from django.db import models

# Create your models here.

class Country(models.Model):
    id = models.AutoField(primary_key=True)
    country = models.CharField(max_length=200)
    status = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)