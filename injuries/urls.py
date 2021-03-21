from django.contrib import admin
from django.conf.urls import url
from . import views

app_name = 'injuries'

urlpatterns = [
    url(r'^$', views.injury_view, name="view_injuries"),
    url(r'^view/(?P<slug>[\w-]+)/$', views.single_injuries, name="single_injuries"),
    url(r'^add/$', views.add_injuries, name="add_injury"),
    url(r'^edit/(?P<slug>[\w-]+)/$', views.edit_injury, name="edit_injuries"),
    url(r'^delete/(?P<id>[\w-]+)/$', views.delete_injury, name="delete_injuries"),
    url(r'^players/$', views.view_players, name="view_players"),
    url(r'^predict/(?P<slug>[\w-]+)/$', views.predict_injury, name="predict_injury"),
    
    
]
