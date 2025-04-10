from django import forms
from .models import Flight, Operator
from datetime import date


class FlightForm(forms.ModelForm):
    class Meta:
        model = Flight
        exclude = ['company']  # we’ll assign company from the logged-in user
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'start_time': forms.TimeInput(attrs={'type': 'time'}),
            'end_time': forms.TimeInput(attrs={'type': 'time'}),
        }


class ReportSelectorForm(forms.Form):
    current_year = date.today().year
    start_year = 2000
    YEARS = [(y, y) for y in range(start_year, current_year + 1)]
    QUARTERS = [("Q1", "Q1"), ("Q2", "Q2"), ("Q3", "Q3"), ("Q4", "Q4")]

    year = forms.ChoiceField(choices=YEARS, label="Year")
    quarter = forms.ChoiceField(choices=QUARTERS, label="Quarter")


class OperatorForm(forms.ModelForm):
    class Meta:
        model = Operator
        exclude = ['company']  # we’ll assign company from the logged-in user
