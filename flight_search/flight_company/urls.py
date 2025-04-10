from django.urls import URLPattern, path

from .views import (
    CreateOperator,
    GetOrUpdateFlight,
    GetOrUpdateOperator,
    CreateFlight,
    OperatorReport,
    ListFlights,
    Passengers,
    ReportSelector,
    ListOperators
)

urlpatterns: list[URLPattern] = [
    path("operators", CreateOperator.as_view(), name="create_operator"),
    path("operators/list", ListOperators.as_view(), name="list_operators"),
    path(
        "operators/<int:operator_id>/", GetOrUpdateOperator.as_view(), name="operators"
    ),
    path("flights/list/", ListFlights.as_view(), name="create_flight"),
    path("flights/", CreateFlight.as_view(), name="list_flights"),
    path("flights/<int:flight_id>/", GetOrUpdateFlight.as_view(), name="flights"),
    path("flights/passengers/<int:flight_id>", Passengers.as_view(), name="list_passengers"),
    path(
        "operators/reports/<int:year>/<str:quarter>/",
        OperatorReport.as_view(),
        name="reports",
    ),
    path('reports/selector', ReportSelector.as_view(), name="report_selector")
]
