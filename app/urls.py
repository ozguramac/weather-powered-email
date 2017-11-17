from django.conf.urls import url

from . import views

urlpatterns = [
    # /app/
    url(r'^$', views.register, name='index'),
]
