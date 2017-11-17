from django.shortcuts import render
from django.db import IntegrityError

from .models import User, Location

def locations():
    return Location.objects.all()

def render_register(request, message=None, error=None):
    return render(request, "register.html", {'locations': locations(), 'error': error, 'message': message})

def register(request):
    if request.method == 'POST':
        email = request.POST.get('email','')
        location = request.POST.get('location','')

        try:
            user = User.objects.create(email=email, location=location)
            user.save()
        except IntegrityError:
            return render_register(request=request, error="You are already registered. Thank you.")

        return render_register(request=request, message="Welcome to Weather Powered Email!")

    return render_register(request=request)
