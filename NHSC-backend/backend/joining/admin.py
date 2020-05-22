from django.contrib import admin
from .models import Joining

# Register your models here.
class JoiningAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'mobile', 'profile_image', 'date', 'aadhar_number', 'aadhar_image', 'about')

# register your model
admin.site.register(Joining, JoiningAdmin)
