from django.contrib import admin
from django.conf.urls import url
from . import views

app_name = 'players'

urlpatterns = [
    url(r'^view/$', views.view_player, name="view"),
    url(r'^profile/(?P<slug>[\w-]+)/$', views.view_profile, name="profile"),
    url(r'^add/$', views.add_player, name="add_player"),
    url(r'^edit/(?P<slug>[\w-]+)/$', views.edit_player, name="edit_player"),
    url(r'^delete/(?P<id>[\w-]+)/$', views.delete_player, name="delete_player"),

]
