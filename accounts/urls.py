from django.conf.urls import url, include
from .views import registration, profile, logout, login

urlpatterns = [
    url(r'^registration/$', registration, name='registration'),
    url(r'^profile/$', profile, name='profile'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^login/$', login, name='login'),
    ]
