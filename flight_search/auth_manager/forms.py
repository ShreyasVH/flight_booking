from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, FlightCompany


class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = ''
        self.fields['email'].required = True

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class CreateFlightCompanyForm(UserCreationForm):
    name = forms.CharField(required=True, max_length=100, label="Comapny Name")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = ''
        self.fields['email'].required = True

    class Meta:
        model = User
        fields = ('name', 'username', 'email', 'password1', 'password2')
