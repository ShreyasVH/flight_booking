from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import User


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
            return render(request, 'auth_manager/login.html', {'error': 'Invalid credentials'})

        user = authenticate(request, username=user.username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('/dashboard/')
        else:
            return render(request, 'auth_manager/login.html', {'error': 'Invalid credentials'})

    def get(self, request):
        return render(request, 'auth_manager/login.html')


class LogoutView(APIView):
    def post(self, request: Request):
        """Logout if its a valid user"""
        ...
        if request.user.is_authenticated:
            auth_logout(request)

        return redirect('/login')


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            # login(request, user)  # optional: logs in the user immediately
            return redirect('/login')  # or a dashboard URL
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
    elif user.role == 'FLIGHT_COMPANY':
        context['company_name'] = user.flight_company.name if user.flight_company else 'N/A'
        template_name = 'auth_manager/dashboard_company.html'
    else:
        template_name = 'auth_manager/dashboard_unknown.html'

    return render(request, template_name, context)
