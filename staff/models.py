from django.db import models

# Create your models here.

class Role(models.Model):
    role = models.CharField(max_length=15, null=False, blank=False)
    
class Status(models.Model):
    status = models.CharField(max_length=15, null=False, blank=False)
    
class TimeTable(models.Model):
    date = models.DateField(null=False, blank=False)
    start_time = models.TimeField(null=False, blank=False)
    end_time = models.TimeField(null=False, blank=False)
    
class User(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField()
    password = models.CharField(max_length=500)
    phone_number = models.PositiveIntegerField()
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name="role")
class Location(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    address = models.CharField(max_length=100, null=False, blank=False)
    timeTable = models.ForeignKey(TimeTable, on_delete=models.CASCADE, related_name="timeTable")
    capacity = models.PositiveIntegerField() 
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    
class Reservation(models.Model):
    timeTable = models.ForeignKey(TimeTable, on_delete=models.CASCADE, related_name="timeTable")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    number_of_people = models.PositiveIntegerField()
    status = models.ForeignKey(Status, on_delete=models.CASCADE, related_name="status")
class Activity(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    status = models.ForeignKey(Status, on_delete=models.CASCADE, related_name="status")
    description = models.CharField(max_length=1000)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    timeTable = models.ForeignKey(TimeTable, on_delete=models.CASCADE, related_name="timeTable")
    hosted_by = models.ForeignKey(User, on_delete=models.CASCADE, relative_name = "user")
    capacity = models.PositiveIntegerField() 
    is_active = models.BooleanField()
    
class Reservation_Location(models.Model):
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE, related_name="reservation")
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name="activity")
    
class Reservation_Activity(models.Model):
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE, related_name="reservation")
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, related_name="activity")
    
class Image_activity(models.Model):
    image = models.ImageField(upload_to="activity")
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, related_name="activity")
    
class Image_location(models.Model):
    image = models.ImageField(upload_to="location")
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name="location")