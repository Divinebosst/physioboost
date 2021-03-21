from django.contrib import admin
from django.conf.urls import url
from . import views

app_name = 'stats'

urlpatterns = [
    url(r'^players/$', views.stats, name="players"),
    url(r'^add/(?P<slug>[\w-]+)/$', views.add_stats, name="add_stats"),
    url(r'^history/(?P<slug>[\w-]+)/$', views.history_stats, name="history_stats"),
    url(r'^edit/(?P<id>[\w-]+)/$', views.edit_stats, name="edit_stats"),
    url(r'^delete/(?P<id>[\w-]+)/$', views.delete_stats, name="delete_stats"),
]
