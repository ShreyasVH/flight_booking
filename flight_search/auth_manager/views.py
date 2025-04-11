from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignUpForm, CreateFlightCompanyForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import User, FlightCompany
from django.contrib import messages
from auth_manager.permissions import IsAdmin


class LoginView(APIView):
    def post(self, request: Request):
        """
        User should pass email and password, check the validity, and if they are valid
        login the user and create a new session id for them. This session id should be sent
        as a cookie in the response.
        """
        ...

        email = request.data.get("email")
        password = request.data.get("password")

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.error(request, 'Invalid credentials')
            return render(request, 'auth_manager/login.html')

        user = authenticate(request, username=user.username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('/dashboard/')
        else:
            messages.error(request, 'Invalid credentials')
            return render(request, 'auth_manager/login.html')

    def get(self, request):
        return render(request, 'auth_manager/login.html')


class LogoutView(APIView):
    def post(self, request: Request):
        """Logout if its a valid user"""
        ...
        if request.user.is_authenticated:
            auth_logout(request)

        return redirect('/user/login')


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Signup successful. Please login')
            return redirect('/user/login')  # or a dashboard URL
    else:
        form = SignUpForm()
    return render(request, 'auth_manager/signup.html', {'form': form})


@login_required
def dashboard_view(request):
    user = request.user
    context = {
        'username': user.username,
        'role': user.role,
    }

    if user.role == 'PASSENGER':
        template_name = 'auth_manager/dashboard_passenger.html'
    elif user.role == 'ADMIN':
        template_name = 'auth_manager/dashboard_admin.html'
    elif user.role == 'FLIGHT_COMPANY':
        context['company_name'] = user.flight_company.name if user.flight_company else 'N/A'
        template_name = 'auth_manager/dashboard_company.html'
    else:
        template_name = 'auth_manager/dashboard_unknown.html'

    return render(request, template_name, context)


class CreateFlightCompanyView(APIView):
    def get(self, request: Request):
        form = CreateFlightCompanyForm()
        return render(request, 'auth_manager/create_flight_company.html', {'form': form})

    def post(self, request: Request):
        form = CreateFlightCompanyForm(request.POST)
        company_name = request.POST.get('name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password1')

        company = FlightCompany.objects.create(name=company_name)
        user = User(
            username=username,
            email=email,
            role='FLIGHT_COMPANY',
            flight_company=company,
            is_active=False
        )
        user.set_password(password)
        user.save()

        messages.success(request, 'Signup successful. You can login once the account is approved')
        return redirect('/user/login')  # or a dashboard URL


class ApprovalListView(APIView):
    permission_classes = [IsAdmin]

    def get(self, request: Request):
        users = User.objects.filter(is_active=False)
        return render(request, 'auth_manager/approval_list.html', {'users': users})


class ApproveUserView(APIView):
    permission_classes = [IsAdmin]

    def post(self, request: Request, user_id: int):
        user = get_object_or_404(User, id=user_id)

        user.is_active = True
        user.save()

        return redirect('/flight_company/approvals')
