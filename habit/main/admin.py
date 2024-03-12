from django.contrib import admin
from .models import Habit,HabitCategory, Category,HabitTracking,Reminder, UserSettings
# Register your models here.
admin.site.register(Habit)
admin.site.register(HabitTracking)
admin.site.register(Category)
admin.site.register(HabitCategory)
admin.site.register(Reminder)
admin.site.register(UserSettings)
