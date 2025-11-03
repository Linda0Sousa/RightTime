from django.db import models

class Role(models.Model):
    role = models.CharField(max_length=15, unique=True)
    

class Status(models.Model):
    status = models.CharField(max_length=15, unique=True)
    
class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=500)
    phone_number = models.PositiveIntegerField(unique=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name="users")
    
class Weekday(models.Model):
    name = models.CharField(max_length=15)
    
class Location(models.Model):
    location = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=8)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    number = models.CharField(max_length=10) 
     
class WeeklySchedule(models.Model):
    weekday = models.ForeignKey(Weekday, on_delete=models.CASCADE, related_name="schedules")
    start_time = models.TimeField()
    end_time = models.TimeField()
    
class AvailableHour(models.Model):
    schedule = models.ForeignKey(WeeklySchedule, on_delete=models.CASCADE, related_name="available_hours")
    start_time = models.TimeField()
    end_time = models.TimeField()
    
class Activity(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    status = models.ForeignKey(Status, on_delete=models.CASCADE, related_name="activities")
    description = models.TextField(max_length=1000)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name="activities")
    hosted_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="hosted_activities")
    capacity = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)
    weeklySchedule = models.ManyToManyField(WeeklySchedule)
    
class Reservation(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, related_name="reservations")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reservations")
    start_time = models.TimeField()
    end_time = models.TimeField()
    number_of_people = models.PositiveIntegerField()
    status = models.ForeignKey(Status, on_delete=models.CASCADE, related_name="reservations")
    created_at = models.DateTimeField(auto_now_add=True)

class ImageActivity(models.Model):
    image = models.ImageField(upload_to="activity")
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, related_name="images")

class ImageLocation(models.Model):
    image = models.ImageField(upload_to="location")
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name="images")
