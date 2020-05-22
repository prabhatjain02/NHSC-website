from django.contrib import admin
from .models import Complaint

# Register your models here.
class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'mobile', 'email', 'gender', 'against', 'subject', 'detail')

# register your model
admin.site.register(Complaint, ComplaintAdmin)
