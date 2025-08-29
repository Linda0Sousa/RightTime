from django.db import models

# Create your models here.
    
class User(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField()
    password = models.CharField(max_length=500)
    phone_number = models.PositiveIntegerField()
    role = models.CharField(
        max_length=20,
        choices=[('staff', "Staff"), ("client", "client")],
    )
class Location(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    address = models.CharField(max_length=100, null=False, blank=False)
    opening_time = models.TimeField(null=False, blank=False)
    closing_time = models.TimeField(null=False, blank=False)
    break_time = models.TimeField(null=True, blank=True)
    image = models.ImageField(upload_to="locations/", blank=False, null=False)
    capacity = models.PositiveIntegerField() 
    
class Session(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField(null=False, blank=False)
    end_time = models.TimeField(null=False, blank=False)
    number_of_people = models.PositiveIntegerField(default= 1)
    status = models.CharField(
        max_length=20,
        choices=[("confirmed", "Confirmed"), ("cancelled", "Cancelled"), ("pendind", "pending")],
        default="confirmed"
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
class Activity(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.CharField(max_length=1000)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField(null=False, blank=False)
    end_time = models.TimeField(null=False, blank=False)
    number_of_people = models.PositiveIntegerField()
    status = models.CharField(
        max_length=20,  
        choices=[("confirmed", "Confirmed"), ("cancelled", "Cancelled"), ("pendind", "pending")],
        default="confirmed"
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    capacity = models.PositiveIntegerField() 