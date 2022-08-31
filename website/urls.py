from django.conf.urls import url, include
from . import views


app_name = 'website'

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^/contact', views.contact, name='contact'),
    url(r'^about', views.about, name='about'),
    url(r'^tours', views.tours, name='tours'),
    url(r'^destinations', views.destinations, name = 'destinations')
]