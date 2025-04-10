from typing import Literal
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from bookings.forms import FlightSearchForm, SeatSelectionForm
from flight_company.models import Flight
from bookings.models import Booking
from rest_framework.permissions import IsAuthenticated
from auth_manager.permissions import IsPassenger
from datetime import datetime, timedelta

class Search(APIView):
    # implement proper permissions here
    permission_classes = [IsAuthenticated, IsPassenger]

    def post(
        self,
        request: Request,
    ) -> Response:
        """
        This is a post call to search flight from a source to a destination on a given date.
        You should take all of these as post arguments.
        Implement filters based on flight operator, number of stops etc...
        Implement sorting based on flight duration or ticket cost...
        """
        ...

    def get(self, request: Request):
        user = request.user

        form = FlightSearchForm(request.GET or None)
        now = datetime.now()
        flights = Flight.objects.filter(start_time__gte=now)

        if form.is_valid():
            source = form.cleaned_data.get('source')
            destination = form.cleaned_data.get('destination')
            date = form.cleaned_data.get('date')

            if source:
                flights = flights.filter(source__icontains=source)
            if destination:
                flights = flights.filter(destination__icontains=destination)
            if date:
                start = datetime.combine(date, datetime.min.time())
                end = start + timedelta(days=1)
                flights = flights.filter(start_time__gte=start, start_time__lt=end)

        return render(request, 'bookings/flight_search.html', {'form': form, 'flights': flights})


class GetOrUpdateBooking(APIView):
    # implement proper permissions here
    permission_classes = [IsAuthenticated, IsPassenger]

    def get(self, request: Request, booking_id: int) -> Response: ...
    def post(self, request: Request, booking_id: int):
        user = request.user
        booking = get_object_or_404(Booking, id=booking_id, passenger=user)

        booking.delete()
        return redirect('/bookings/my')
    def delete(self, request: Request, booking_id: int) -> Response: ...


class MyBookings(APIView):
    # implement proper permissions here
    permission_classes = [IsAuthenticated, IsPassenger]

    def get(self, request: Request):
        user = request.user
        now = datetime.now()
        bookings = Booking.objects.select_related('flight').filter(passenger=user, flight__start_time__gte=now).order_by('flight__start_time')

        return render(request, 'bookings/my_bookings.html', {'bookings': bookings})


class CreateBooking(APIView):
    # implement proper permissions here
    permission_classes = [IsAuthenticated, IsPassenger]

    def post(self, request: Request, flight_id):
        user = request.user

        flight = get_object_or_404(Flight, id=flight_id)

        # Prevent duplicate booking
        if Booking.objects.filter(passenger=user, flight=flight).exists():
            return redirect('/search/')

        total_seats = 30
        booked_seats = Booking.objects.filter(flight=flight).values_list('seat_number', flat=True)
        available_seats = [i for i in range(1, total_seats + 1) if i not in booked_seats]

        form = SeatSelectionForm(available_seats, request.POST)
        if form.is_valid():
            seat_number = form.cleaned_data['seat_number']
            Booking.objects.create(passenger=user, flight=flight, seat_number=seat_number)
            return redirect('/search/')

    def get(self, request: Request, flight_id):
        user = request.user

        flight = get_object_or_404(Flight, id=flight_id)

        # Prevent duplicate booking
        if Booking.objects.filter(passenger=user, flight=flight).exists():
            return redirect('/search/')

        total_seats = 30
        booked_seats = Booking.objects.filter(flight=flight).values_list('seat_number', flat=True)
        available_seats = [i for i in range(1, total_seats + 1) if i not in booked_seats]

        form = SeatSelectionForm(available_seats)

        return render(request, 'bookings/select_seat.html', {
            'flight': flight,
            'form': form
        })