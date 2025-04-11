from django import forms
from .models import Flight, Operator
from datetime import date, datetime
from django.utils import timezone


class FlightForm(forms.ModelForm):
    class Meta:
        model = Flight
        exclude = ['company']  # we’ll assign company from the logged-in user
        widgets = {
            'start_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

    def __init__(self, *args, **kwargs):
        company = kwargs.pop('company', None)
        super().__init__(*args, **kwargs)

        if company:
            self.fields['operator'].queryset = Operator.objects.filter(company=company)

        now = timezone.now().strftime('%Y-%m-%dT%H:%M')

        self.fields['start_time'].widget.attrs['min'] = now
        self.fields['end_time'].widget.attrs['min'] = now

    def clean(self):
        cleaned_data = super().clean()
        start_time = cleaned_data.get("start_time")
        end_time = cleaned_data.get("end_time")

        if start_time and end_time and end_time <= start_time:
            raise forms.ValidationError("End time must be after start time.")


class ReportSelectorForm(forms.Form):
    current_year = date.today().year
    start_year = 2000
    YEARS = [(y, y) for y in range(current_year, start_year - 1, -1)]
    QUARTERS = [("Q1", "Q1"), ("Q2", "Q2"), ("Q3", "Q3"), ("Q4", "Q4")]

    year = forms.ChoiceField(choices=YEARS, label="Year")
    quarter = forms.ChoiceField(choices=QUARTERS, label="Quarter")
    operator = forms.ChoiceField()

    def __init__(self, *args, **kwargs):
        company = kwargs.pop('company', None)
        super().__init__(*args, **kwargs)

        if company:
            self.fields['operator'].choices = [(operator.id, f"{operator.first_name} {operator.last_name}")  for operator in Operator.objects.filter(company=company)]


class OperatorForm(forms.ModelForm):
    class Meta:
        model = Operator
        exclude = ['company']  # we’ll assign company from the logged-in user
