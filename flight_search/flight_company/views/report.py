from typing import Literal
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

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
    permission_classes = []

    def get(
        self,
        request: Request,
        operator_id: int,
        year: int,
        quarter: Literal["Q1", "Q2", "Q3", "Q4"],
    ) -> Response:
        """
        Generate some stats here. The schema of these stats is defined in
        the above base model class `OperatorStats`. your response should contains
        all the stats from this class.
        """
        ...
