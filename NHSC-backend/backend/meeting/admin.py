from django.contrib import admin
from .models import Meeting

# Register your models here.
class MeetingAdmin(admin.ModelAdmin):
    list_display = ('title', 'held_on')

# register your model
admin.site.register(Meeting, MeetingAdmin)
