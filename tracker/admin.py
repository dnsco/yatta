from django.contrib import admin

from .models import Activity, ActivityEvent

admin.site.register(Activity)
admin.site.register(ActivityEvent)
