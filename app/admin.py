from django.contrib import admin

from app.emailer import send_wxmail
from .models import User, Location

def send_weather_emails(modeladmin, request, queryset):
    for user in queryset:
        send_wxmail(user)

    modeladmin.message_user(request, "Successfully sent emails to %s subscriber(s)." % len(queryset))
    return


send_weather_emails.short_description = "Send Weather-Powered Emails to Users"

class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'location']
    ordering = ['email']
    actions = [send_weather_emails]

admin.site.register(User, UserAdmin)
