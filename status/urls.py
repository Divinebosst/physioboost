from django.contrib import admin
from django.conf.urls import url
from . import views

app_name = 'status'

urlpatterns = [
    url(r'^players/$', views.status, name="players"),
    url(r'^edit/(?P<slug>[\w-]+)/$', views.edit_player_status, name="edit_player_status"),
    url(r'^tracker/$', views.tracker, name="tracker"),
]
