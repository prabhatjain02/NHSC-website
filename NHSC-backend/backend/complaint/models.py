from django.db import models

GENDER_CHOICES = (
    ('male', 'MALE'),
    ('female', 'FEMALE'),
    ('other', 'OTHER'),
)

# Create your models here.

class Complaint(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    mobile = models.CharField(max_length=10)
    email = models.EmailField()
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default='male')
    against = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    detail = models.CharField(max_length=500)
    