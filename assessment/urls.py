from django.contrib import admin
from django.conf.urls import url
from . import views

app_name = 'assessment'

urlpatterns = [
    url(r'^$', views.assess, name="view_assess"),
    url(r'^players/$', views.player_assessment, name="player_assessment"),
    url(r'^assess/(?P<slug>[\w-]+)/$', views.add_assessment, name="add_assessment"),
    url(r'^edit/(?P<slug>[\w-]+)/$', views.edit_assessment, name="edit_assessment"),
    url(r'^view/(?P<id>[\w-]+)/$', views.single_assessment, name="single_assessment"),
]