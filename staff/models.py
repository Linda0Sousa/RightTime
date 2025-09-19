from django.db import models

# Create your models here.

class Role(models.Model):
    role = models.CharField(max_length=15, null=False, blank=False)
    
class Status(models.Model):
    status = models.CharField(max_length=15, null=False, blank=False)
class User(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=500)
    phone_number = models.PositiveIntegerField(unique=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name="users")
    
class TimeTable(models.Model):
    date = models.DateField(null=False, blank=False)
    start_time = models.TimeField(null=False, blank=False)
    end_time = models.TimeField(null=False, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="timeTable")
    
class Location(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    address = models.CharField(max_length=100, null=False, blank=False)
    timeTable = models.ForeignKey(TimeTable, on_delete=models.CASCADE, related_name="locations")
    capacity = models.PositiveIntegerField() 
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="locations")
    description = models.CharField(max_length=1000)
    
class Weekdays(models.Model):
    name = models.CharField(max_length=15)
    
class WeeklySchedule(models.Model):
    day = models.ForeignKey(Weekdays, on_delete=models.CASCADE, related_name="schedules")
    start_time = models.TimeField()
    end_time = models.TimeField()
    location = models.ForeignKey("Location", on_delete=models.CASCADE, related_name="weekly_schedules")
    
class Reservation(models.Model):
    timeTable = models.ForeignKey(TimeTable, on_delete=models.CASCADE, related_name="reservations")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reservations")
    number_of_people = models.PositiveIntegerField()
    status = models.ForeignKey(Status, on_delete=models.CASCADE, related_name="reservations")
    
class Activity(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    status = models.ForeignKey(Status, on_delete=models.CASCADE, related_name="activities")
    description = models.CharField(max_length=1000)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    timeTable = models.ForeignKey(TimeTable, on_delete=models.CASCADE, related_name="activities")
    hosted_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "user")
    capacity = models.PositiveIntegerField() 
    is_active = models.BooleanField()
    
class Reservation_Location(models.Model):
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE, related_name="reservations_locations")
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name="reservations_locations")
    
class Reservation_Activity(models.Model):
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE, related_name="reservations_activities")
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, related_name="reservations_activities")
    
class Image_activity(models.Model):
    image = models.ImageField(upload_to="activity")
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, related_name="image_activities")
    
class Image_location(models.Model):
    image = models.ImageField(upload_to="location")
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name="image_locations")