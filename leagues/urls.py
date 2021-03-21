from django.contrib import admin
from django.conf.urls import url
from . import views

app_name = 'leagues'

urlpatterns = [
    url(r'^view/$', views.view_leagues, name="view_leagues"),
]