import requests

from django.shortcuts import render
from django.db import IntegrityError

from .emailer import send_wxmail
from .models import User, Location
from .settings import RECAPTCHA_SECRET_KEY, RECAPTCHA_SITE_KEY

def locations():
    return Location.objects.all()

def render_register(request, message=None, error=None):
    return render(request, "register.html", {'locations': locations(), 'error': error, 'message': message,
                                             'reCAPTCHA_site_key': RECAPTCHA_SITE_KEY})

def register(request):
    if request.method == 'POST':
        email = request.POST.get('email','')
        location = request.POST.get('location','')

        throttle_token = request.POST.get('throttle_token','')
        r = requests.post('https://www.google.com/recaptcha/api/siteverify',
                                        data={'secret': RECAPTCHA_SECRET_KEY, 'response': throttle_token})
        if r.status_code == requests.codes.ok:
            throttle_verify = r.json()
            if not throttle_verify[ 'success']:
                return render_register(
                    request=request, error="Throttle failure: {} - {}".format(
                        r.status_code, throttle_verify['error-codes']))

        try:
            coords = location.split(',')
            if len(coords) == 2:
                curLoc = Location.objects.create(city='',state='',latitude=float(coords[0]), longtitude=float(coords[1]))
                curLoc.save()
                location = curLoc.id
            user = User.objects.create(email=email, location=location)
            user.save()
            send_wxmail(user)
        except IntegrityError:
            return render_register(request=request, error="You are already registered. Thank you.")

        return render_register(request=request, message="Welcome to Weather Powered Email!")

    return render_register(request=request)
