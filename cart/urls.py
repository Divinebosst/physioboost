from django.conf.urls import url
from . import views

app_name = 'cart'

urlpatterns = [
    url(r'^$', views.pay, name="home"),
    url(r'^done/$', views.payment_done, name="done"),
    url(r'^canceled/$', views.payment_canceled, name="canceled"),

]