from django.urls import URLPattern, path
from .views import LoginView, LogoutView, signup_view, dashboard_view
from django.contrib.auth.views import LoginView as LoginUIView, LogoutView as LogoutUIView

urlpatterns: list[URLPattern] = [
    path("user/login/", LoginView.as_view(), name="login"),
    path("user/logout/", LogoutView.as_view(), name="logout"),
    path('signup/', signup_view, name='signup'),
    path('dashboard/', dashboard_view, name='dashboard'),
]
