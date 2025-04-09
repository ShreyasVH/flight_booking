from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, FlightCompany


class SignUpForm(UserCreationForm):
    role = forms.ChoiceField(choices=User.ROLE_CHOICES)
    flight_company = forms.ModelChoiceField(
        queryset=FlightCompany.objects.all(),
        required=False,
        help_text="Required only if registering as a Flight Company user"
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'role', 'flight_company', 'password1', 'password2')
