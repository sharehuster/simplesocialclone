from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from simplesocial import settings

app_name = 'accounts'

urlpatterns = [
    path("login", auth_views.LoginView.as_view(template_name = 'accounts/login.html'), name = 'login'),
    path("signup", views.SignUp.as_view(), name = 'signup'),
    path("logout", auth_views.LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name = 'logout'),
]
