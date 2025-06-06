from django.db import models
from django.contrib.auth.models import User

class Job(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} at {self.company}"


class Application(models.Model):
    EDUCATION_CHOICES = [
        ('8th', '8th'),
        ('10th', '10th'),
        ('12th', '12th'),
        ('diploma', 'Diploma'),
        ('undergraduate', 'Undergraduate'),
        ('graduate', 'Graduate'),
        ('postgraduate', 'Postgraduate'),
    ]

    EXPERIENCE_CHOICES = [
        ('fresher', 'Fresher'),
        ('working', 'Working Professional'),
        ('student', 'College Student'),
    ]

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    dob = models.DateField(default='2000-01-01')
    education = models.CharField(max_length=20, choices=EDUCATION_CHOICES)
    experience = models.CharField(max_length=20, choices=EXPERIENCE_CHOICES)
    resume = models.FileField(upload_to='resumes/')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} applied for {self.job.title}'
