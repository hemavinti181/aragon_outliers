from django.db import models

# Create your models here.

class Country(models.Model):
    id = models.AutoField(primary_key=True)
    country = models.CharField(max_length=200)
    status = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class State(models.Model):
    id = models.AutoField(primary_key=True)
    country = models.ForeignKey(Country, null=True, blank=True, on_delete=models.SET_NULL, related_name='state')
    state = models.CharField(max_length=200)
    status = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class City(models.Model):
    id = models.AutoField(primary_key=True)
    country = models.ForeignKey(Country, null=True, blank=True, on_delete=models.SET_NULL, related_name='city')
    state = models.ForeignKey(State, null=True, blank=True, on_delete=models.SET_NULL, related_name='cities')
    city = models.CharField(max_length=200)
    deleted = models.BooleanField(default=False)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Area(models.Model):
    id = models.AutoField(primary_key=True)
    country = models.ForeignKey(Country, null=True, blank=True, on_delete=models.SET_NULL, related_name='area_country')
    state = models.ForeignKey(State, null=True, blank=True, on_delete=models.SET_NULL, related_name='area_state')
    city = models.ForeignKey(City, null=True, blank=True, on_delete=models.SET_NULL, related_name='area_city')
    area = models.CharField(max_length=200)
    deleted = models.BooleanField(default=False)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)