from django.contrib import admin
from .models import Notices

# Register your models here.
class NoticeAdmin(admin.ModelAdmin):
    list_display = ('published_date', 'title')


# registering the model
admin.site.register(Notices, NoticeAdmin)