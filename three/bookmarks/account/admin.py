from django.contrib import admin
from .models import Activity

# Register your models here.
@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'start_time', 'stop_time')
    list_filter = ('name', 'date')
    search_fields = ('name',)

