from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render, redirect
from flight_company.forms import FlightForm
from flight_company.models import Flight


class GetOrUpdateFlight(APIView):
    # implement proper permissions here
    permission_classes = []

    def get(self, request: Request, flight_id: int) -> Response:
        """
        This will fetch all the details for a flight.
        """
        ...

    def post(self, request: Request, flight_id: int) -> Response:
        """
        This will update all the details for a flight.
        """
        ...

    def delete(self, request: Request, flight_id: int) -> Response:
        """
        This view will delete a flight operation.

        Once this flight is deleted, you will need update the flight graph
        Such that in the next search, this flight is removed
        """
        ...


class CreateFlight(APIView):
    # implement proper permissions here
    permission_classes = []

    def post(self, request: Request):
        """
        This view will register a new flight operation from a operator
        Its a post call, hence will have some post params like
        flight_model, source, destination, operator, cost, flight time etc...

        Once this flight is added, you will need update the flight graph
        Such that in the next search, this flight is added
        """
        ...
        user = request.user
        form = FlightForm(request.POST)
        if form.is_valid():
            flight = form.save(commit=False)
            flight.company = user.flight_company
            flight.save()

        return redirect('/dashboard/')

    def get(self, request: Request):
        user = request.user

        if user.role != 'FLIGHT_COMPANY':
            return redirect('/auth/dashboard/')

        form = FlightForm()

        return render(request, 'flight_company/create_flight.html', {'form': form})


class ListFlights(APIView):
    def get(self, request: Request):
        """
        This will fetch all the details for a flight.
        """
        ...
        user = request.user

        if user.role != 'FLIGHT_COMPANY':
            return redirect('/dashboard/')

        flights = Flight.objects.filter(company=user.flight_company).order_by('date', 'start_time')

        return render(request, 'flight_company/view_flights.html', {'flights': flights})

    def post(self, request: Request, flight_id: int) -> Response:
        """
        This will update all the details for a flight.
        """
        ...

    def delete(self, request: Request, flight_id: int) -> Response:
        """
        This view will delete a flight operation.

        Once this flight is deleted, you will need update the flight graph
        Such that in the next search, this flight is removed
        """
        ...