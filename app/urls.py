from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    # /
    url(r'^$', views.register, name='index'),
    url(r'^admin/', admin.site.urls),
]
