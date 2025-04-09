from django.urls import URLPattern, path

from .views import (
    CreateOperator,
    GetOrUpdateFlight,
    GetOrUpdateOperator,
    CreateFlight,
    OperatorReport,
)

urlpatterns: list[URLPattern] = [
    path("operators/", CreateOperator.as_view(), name="create_operator"),
    path(
        "operators/<int:operator_id>/", GetOrUpdateOperator.as_view(), name="operators"
    ),
    path("flights/", CreateFlight.as_view(), name="create_flight"),
    path("flights/<int:flight_id>/", GetOrUpdateFlight.as_view(), name="flights"),
    path(
        "operators/<int:operator_id>/reports/<int:year>/<str:quarter>/",
        OperatorReport.as_view(),
        name="reports",
    ),
]
