from django.db import models


# Create your models here.

class Notices(models.Model):
    published_date = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=200)

