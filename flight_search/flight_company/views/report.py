from typing import Literal
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from auth_manager.permissions import IsFlightCompany
from datetime import datetime, timedelta
from flight_company.models import Flight
from bookings.models import Booking
import csv
from django.http import HttpResponse
from flight_company.forms import ReportSelectorForm
from django.shortcuts import render, redirect

from pydantic import BaseModel


class OperatorStats(BaseModel):
    year: int
    quarter: Literal["Q1", "Q2", "Q3", "Q4"]
    total_flights: int
    total_passengers: int
    total_hours_of_flight: float
    revenue: float


class OperatorReport(APIView):
    # implement proper permissions here
    permission_classes = [IsAuthenticated, IsFlightCompany]

    def get(
        self,
        request: Request,
        operator_id: int,
        year: int,
        quarter: Literal["Q1", "Q2", "Q3", "Q4"],
    ):
        """
        Generate some stats here. The schema of these stats is defined in
        the above base model class `OperatorStats`. your response should contains
        all the stats from this class.
        """
        user = request.user

        quarter_map = {
            "Q1": (1, 3),
            "Q2": (4, 6),
            "Q3": (7, 9),
            "Q4": (10, 12),
        }

        start_month, end_month = quarter_map[quarter]

        start_date = datetime(year, start_month, 1).date()
        if end_month == 12:
            end_date = datetime(year + 1, 1, 1).date()
        else:
            end_date = datetime(year, end_month + 1, 1).date()

        flights = Flight.objects.filter(
            operator_id=operator_id,
            date__gte=start_date,
            date__lt=end_date,
        )

        now = datetime.now()
        total_hours = 0.0
        flight_ids = []
        for flight in flights:
            dt_start = datetime.combine(flight.date, flight.start_time)
            dt_end = datetime.combine(flight.date, flight.end_time)
            if dt_end < dt_start:
                dt_end += timedelta(days=1)

            if dt_end < now:
                flight_ids.append(flight.id)
                duration_hours = (dt_end - dt_start).total_seconds() / 3600
                total_hours += duration_hours

        total_flights = len(flight_ids)
        bookings = Booking.objects.filter(flight_id__in=flight_ids)
        total_passengers = bookings.count()
        revenue = sum(b.flight.cost for b in bookings)

        stats = OperatorStats(
            year=year,
            quarter=quarter,
            total_flights=total_flights,
            total_passengers=total_passengers,
            total_hours_of_flight=round(total_hours, 2),
            revenue=float(revenue),
        )

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename="report_{year}_{quarter}_{operator_id}.csv"'

        writer = csv.writer(response)
        writer.writerow(["Year", "Quarter", "Total Flights", "Total Passengers", "Total Hours", "Revenue"])
        writer.writerow([
            stats.year,
            stats.quarter,
            stats.total_flights,
            stats.total_passengers,
            stats.total_hours_of_flight,
            stats.revenue
        ])
        return response


class ReportSelector(APIView):
    # implement proper permissions here
    permission_classes = [IsAuthenticated, IsFlightCompany]

    def get(self, request: Request):
        user = request.user
        form = ReportSelectorForm(company=user.flight_company)
        return render(request, 'flight_company/select_report.html', {'form': form})

    def post(self, request):
        user = request.user
        form = ReportSelectorForm(request.POST, company=user.flight_company)
        if form.is_valid():
            year = form.cleaned_data['year']
            quarter = form.cleaned_data['quarter']
            operator_id = form.cleaned_data['operator']

            return redirect(f'/operators/{operator_id}/reports/{year}/{quarter}/')

        return render(request, 'flight_company/select_report.html', {'form': form})
