import requests
from django.core.mail import send_mail

from .models import Location
from .settings import WEATHER_API_KEY, EMAIL_HOST, EMAIL_HOST_USER


def send_wxmail(user):
    loc = Location.objects.get(id=user.location)
    wak = WEATHER_API_KEY
    from_email = EMAIL_HOST_USER + '@' + EMAIL_HOST
    temp = 72
    weather = 'Sunny'
    temp_avg = 70
    if wak != '':
        url = 'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=imperial&&appid={key}' \
            .format(key=wak, lat=loc.latitude, lon=loc.longtitude)
        resp = requests.get(url).json()

        temp = resp['main']['temp']
        weather = resp['weather'][0]['main']

        temp_avg = (int(resp['main']['temp_max']) + int(resp['main']['temp_min'])) / 2
    if weather == 'Clear' or temp_avg + 5 <= temp:
        subject = "It's nice out! Enjoy a discount on us."
    elif "Rain" in weather or temp <= temp_avg - 5:
        subject = "Not so nice out? That's okay, enjoy a discount on us."
    else:
        subject = "Enjoy a discount on us."
    message = "Current temperature is {temp} with {weather} at your location {city} {state}.".format(
        city=loc.city, state=loc.state, temp=temp, weather=weather)
    send_mail(subject, message, from_email, [user.email], fail_silently=False)