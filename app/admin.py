from django.contrib import admin

import os
import requests

from datetime import datetime, timedelta
from django.core.mail import send_mail

from .models import User, Location

wak = os.getenv('WUNDERGROUND_API_KEY')
from_email = os.getenv('EMAIL_USER') + '@' + os.getenv('EMAIL_HOST')

def send_weather_emails(modeladmin, request, queryset):
    for user in queryset:
        loc = Location.objects.get(id=user.location);

        temp = 72
        weather = 'Sunny'
        temp_avg = 70
        if wak != '':
            url = 'https://api.wunderground.com/api/{key}/geolookup/conditions/q/{state}/{city}.json' \
                .format(key=wak, state=loc.state, city=loc.city)
            resp = requests.get(url).json()

            temp = resp['current_observation']['temp_f']
            weather = resp['current_observation']['weather']

            now = datetime.utcnow()
            date_range = "%s%s" % ((now - timedelta(days=30)).strftime("%m%d"), now.strftime("%m%d"))
            url = 'https://api.wunderground.com/api/{key}/planner_{date_range}/q/{state}/{city}.json' \
                .format(key=wak, date_range=date_range, state=loc.state, city=loc.city)
            resp = requests.get(url).json()

            temp_avg = (int(resp['trip']['temp_high']['avg']['F']) + int(resp['trip']['temp_low']['avg']['F']))/2

        if weather == 'Clear' or temp_avg + 5 <= temp:
            subject = "It's nice out! Enjoy a discount on us."
        elif "Rain" in weather or temp <= temp_avg - 5:
            subject ="Not so nice out? That's okay, enjoy a discount on us."
        else:
            subject = "Enjoy a discount on us."

        message = "Current temperature in {city}, {state} is {temp}, {weather}." \
            .format(city=loc.city, state=loc.state, temp=temp, weather=weather)

        send_mail(subject, message, from_email, [user.email],fail_silently=False)

    modeladmin.message_user(request, "Successfully sent emails to %s subscriber(s)." % len(queryset))
    return
send_weather_emails.short_description = "Send Weather-Powered Emails to Users"

class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'location']
    ordering = ['email']
    actions = [send_weather_emails]

admin.site.register(User, UserAdmin)
