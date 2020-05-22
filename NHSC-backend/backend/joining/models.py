from django.db import models
import os

def get_image_path(instance, filename):
    return os.path.join('photos', str(instance.id), filename)

# Create your models here.
class Joining(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    email = models.EmailField()
    mobile = models.CharField(max_length=10)
    profile_image = models.ImageField(upload_to=get_image_path)
    date = models.DateField(auto_now_add=True)
    aadhar_number = models.IntegerField(null=False, blank=False, unique=True)
    aadhar_image = models.ImageField(upload_to=get_image_path)
    about = models.CharField(max_length=250)
