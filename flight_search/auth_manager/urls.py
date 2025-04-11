from django.urls import URLPattern, path
from .views import LoginView, LogoutView, signup_view, dashboard_view, CreateFlightCompanyView, ApprovalListView, ApproveUserView
from django.contrib.auth.views import LoginView as LoginUIView, LogoutView as LogoutUIView

urlpatterns: list[URLPattern] = [
    path("user/login/", LoginView.as_view(), name="login"),
    path("user/logout/", LogoutView.as_view(), name="logout"),
    path('signup/', signup_view, name='signup'),
    path('flight_company/create/', CreateFlightCompanyView.as_view(), name='create_flight_company'),
    path('flight_company/approvals/', ApprovalListView.as_view(), name='flight_company_approvals'),
    path('flight_company/approve/<int:user_id>', ApproveUserView.as_view(), name='flight_company_approve'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('', dashboard_view, name='home'),
]
