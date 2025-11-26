from django.contrib import admin
from .models import Coach, Location, Student, Attendance

@admin.register(Coach)
class CoachAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ['name', 'coach', 'time_slot']

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'age', 'fees_paid']

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ['student', 'date', 'present']