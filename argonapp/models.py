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
    zipcode = models.TextField(max_length=8, null=True, blank=True)
    deleted = models.BooleanField(default=False)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Amenities(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    type = models.TextField(max_length=1000, null=True, blank=True)
    status = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Property_types(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    status = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Nearby_Landmark(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    status = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Property_for(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    status = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Package(models.Model):
    id = models.AutoField(primary_key=True)
    package_name = models.CharField(max_length=200)
    package_price = models.TextField(max_length=100, null=True, blank=True)
    package_life = models.TextField(max_length=100, null=True, blank=True)
    package_type = models.TextField(max_length=100, null=True, blank=True)
    applicable_for = models.TextField(max_length=100, null=True, blank=True)
    status = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)