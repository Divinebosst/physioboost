from django.conf.urls import url, include
from django.contrib import admin
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from account import views as do_login
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView, PasswordResetCompleteView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^dashboard/', include('dashboard.urls')),
    url(r'^leagues/', include('leagues.urls')),
    url(r'^clubs/', include('clubs.urls')),
    url(r'^players/', include('players.urls')),
    url(r'^account/', include('account.urls')),
    url(r'^paypal/', include('paypal.standard.ipn.urls')),
    url(r'^cart/', include('cart.urls')),
    url(r'^articles/', include('articles.urls')),
    url(r'^injuries/', include('injuries.urls')),
    url(r'^assessment/', include('assessment.urls')),
    url(r'^stats/', include('stats.urls')),
    url(r'^status/', include('status.urls')),
    url(r'^about/$', views.about),
    url(r'^$', do_login.login_view, name="home"),
    url(r'^reset-password/$', PasswordResetView.as_view(template_name='account/reset-password.html'), name='reset_password'),
    url(r'^reset-password/done/$', PasswordResetDoneView.as_view(template_name='account/reset-password-done.html'), name='password_reset_done'),
    url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z].+)/$', PasswordResetConfirmView.as_view(template_name='account/reset-password-confirm.html'), name='password_reset_confirm'),
    url(r'^reset-password/complete/$', PasswordResetCompleteView.as_view(template_name='account/reset-password-complete.html'), name='password_reset_complete'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
