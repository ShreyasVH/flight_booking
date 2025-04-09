from django import forms


class FlightSearchForm(forms.Form):
    source = forms.CharField(required=False, max_length=100)
    destination = forms.CharField(required=False, max_length=100)
    date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))


class SeatSelectionForm(forms.Form):
    seat_number = forms.ChoiceField(label="Select a seat")

    def __init__(self, available_seats, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['seat_number'].choices = [(s, f"Seat {s}") for s in available_seats]
