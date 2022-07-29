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

class Property(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    short_description = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    built_up_area_price = models.CharField(max_length=100)
    property_type = models.CharField(max_length=100)
    property_for = models.CharField(max_length=100)
    property_added_by_user_type = models.CharField(max_length=100)
    property_user_id_added = models.IntegerField()
    lat = models.FloatField(max_length=100)
    long = models.FloatField(max_length=100)
    address = models.CharField(max_length=1000)
    country = models.IntegerField(max_length=10)
    state = models.IntegerField(max_length=10)
    city = models.IntegerField(max_length=10)
    zipcode = models.CharField(max_length=100)
    sub_area = models.IntegerField(max_length=10)
    size = models.CharField(max_length=100)
    built_up_area_size = models.CharField(max_length=100)
    bed_rooms = models.CharField(max_length=100)
    bath_rooms = models.CharField(max_length=100)
    parking_slots = models.CharField(max_length=100)
    status = models.IntegerField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    unique_id = models.CharField(max_length=100)
    indoor_amenities = models.CharField(max_length=100)
    outdoor_amenities = models.CharField(max_length=100)
    deleted = models.BooleanField(default=False)

class Users(models.Model):
    id = models.AutoField(primary_key=True)
    unique_id = models.CharField(max_length=100)
    user_name = models.CharField(max_length=1000)
    user_full_name = models.CharField(max_length=1000)
    user_pass = models.CharField(max_length=1000)
    user_email = models.CharField(max_length=100)
    user_mobile = models.CharField(max_length=100)
    user_type = models.CharField(max_length=100)
    user_registered_date = models.CharField(max_length=1000)
    user_verified = models.FloatField(max_length=100)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)