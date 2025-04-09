from typing import Literal
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView


class Search(APIView):
    # implement proper permissions here
    permission_classes = []

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


class GetOrUpdateBooking(APIView):
    # implement proper permissions here
    permission_classes = []

    def get(self, request: Request, booking_id: int) -> Response: ...
    def post(self, request: Request, booking_id: int) -> Response: ...
    def delete(self, request: Request, booking_id: int) -> Response: ...


class CreateBooking(APIView):
    # implement proper permissions here
    permission_classes = []

    def post(self, request: Request) -> Response: ...
