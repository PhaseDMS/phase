from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView

from .forms import EmailAuthenticationForm


urlpatterns = [
    path('login/$',
        LoginView.as_view(authentication_form=EmailAuthenticationForm),
        name='login'),
    path('logout/$',
        auth_views.logout_then_login,
        name='logout'),
    path('password-reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$',
        auth_views.password_reset_confirm,
        name='password_reset_confirm'),
    path('password-reset-complete/$',
        auth_views.password_reset_complete,
        name='password_reset_complete'),
    path('password-change/$',
        auth_views.password_change,
        {'post_change_redirect': '/'},
        name='password_change')
]
