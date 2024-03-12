from django.db import models
from django.contrib.auth.models import User
# Create your models here.
#habits users want to track
class Habit(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    frequency = models.CharField(max_length=20)  # e.g., daily, weekly
    start_date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
      return self.name
    #categories
class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
      return self.name
class HabitCategory(models.Model):
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    def __str__(self):
       return f"{self.habit.name} - {self.category.name}"

class HabitTracking(models.Model):
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    successful = models.BooleanField(default=False)
    notes = models.TextField(blank=True, null=True)
    def __str__(self):
      return f"{self.habit.name} - {self.timestamp}"

class Reminder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE)
    time = models.TimeField()
    active = models.BooleanField(default=True)
    def __str__(self):
      return f"{self.user.username} - {self.habit.name} - {self.time}"

class UserSettings(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    timezone = models.CharField(max_length=50)
    language = models.CharField(max_length=50)
    def __str__(self):
     return self.user.username
