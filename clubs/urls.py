from django.contrib import admin
from django.conf.urls import url
from . import views

app_name = 'clubs'

urlpatterns = [
    url(r'^view/(?P<id>[\w-]+)/$', views.view_clubs, name="view_clubs"),
]
