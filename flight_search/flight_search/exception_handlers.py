from rest_framework.views import exception_handler
from rest_framework.exceptions import PermissionDenied, NotAuthenticated
from django.shortcuts import render, redirect


def custom_exception_handler(exc, context):
    request = context.get("request")

    print('exception')
    print(exc)
    print(type(exc))

    if isinstance(exc, NotAuthenticated):
        # Redirect HTML views, fallback to JSON for API clients
        print('logged out')
        return redirect('/user/login')
    if isinstance(exc, PermissionDenied):
        # Redirect HTML views, fallback to JSON for API clients
        print('permission denied')
        return render(request, '403.html', status=403)

    return exception_handler(exc, context)
