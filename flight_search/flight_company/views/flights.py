from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render, redirect, get_object_or_404
from flight_company.forms import FlightForm
from flight_company.models import Flight
from rest_framework.permissions import IsAuthenticated


class GetOrUpdateFlight(APIView):
    # implement proper permissions here
    permission_classes = [IsAuthenticated]

    def get(self, request: Request, flight_id: int) -> Response:
        """
        This will fetch all the details for a flight.
        """
        ...

        user = request.user
        flight = get_object_or_404(Flight, id=flight_id, company=user.flight_company)

        form = FlightForm(instance=flight)
        return render(request, 'flight_company/edit_flight.html', {'form': form, 'flight': flight})

    def post(self, request: Request, flight_id: int) -> Response:
        """
        This will update all the details for a flight.
        """
        ...
        user = request.user
        flight = get_object_or_404(Flight, id=flight_id, company=user.flight_company)

        if request.POST.get("_method") == "DELETE":
            flight.delete()
            return redirect('/flights/list/')

        form = FlightForm(request.POST, instance=flight)
        if form.is_valid():
            form.save()
            return redirect('/flights/list/')
        return render(request, 'flight_company/edit_flight.html', {'form': form, 'flight': flight})


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