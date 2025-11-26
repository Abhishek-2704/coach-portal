from django.db import models
from django.contrib.auth.models import User

class Coach(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Location(models.Model):
    coach = models.ForeignKey(Coach, on_delete=models.CASCADE, related_name='locations')
    name = models.CharField(max_length=100)
    time_slot = models.CharField(max_length=50)

    class Meta:
        unique_together = ('coach', 'name')

    def __str__(self):
        return f"{self.name} - {self.time_slot}"

class Student(models.Model):
    BLOOD_GROUPS = [
        ('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'),
        ('O+', 'O+'), ('O-', 'O-'), ('AB+', 'AB+'), ('AB-', 'AB-'),
    ]

    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='students')
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUPS)
    fees_paid = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    present = models.BooleanField(default=False)

    class Meta:
        unique_together = ('student', 'date')