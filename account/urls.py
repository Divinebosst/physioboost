from django.conf.urls import url
from . import views
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

app_name = 'account'

urlpatterns = [
    url(r'^signup/$', views.signup_view, name="signup"),
    url(r'^login/$', views.login_view, name="login"),
    url(r'^logout/$', views.logout_view, name="logout"),
    url(r'^profile/$', views.view_profile, name='view_profile'),
    url(r'^profile/edit$', views.edit_profile, name='edit_profile'),
    url(r'^change-password/$', views.change_password, name='change_password'),
]