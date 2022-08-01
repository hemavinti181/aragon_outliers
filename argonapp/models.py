from django.db import models

# Create your models here.
class User(models.Model):

    id=models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=20)
    Username = models.CharField(max_length=20)
    Email = models.EmailField(max_length=20)
    Phone_number = models.CharField(max_length=10)
    address = models.CharField(max_length=50)
    Status_Boolean = models.BooleanField()
    Created_at = models.DateTimeField()
    Updated_at = models.DateTimeField()
