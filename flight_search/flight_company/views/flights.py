from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView


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

    def post(self, request: Request) -> Response:
        """
        This view will register a new flight operation from a operator
        Its a post call, hence will have some post params like
        flight_model, source, destination, operator, cost, flight time etc...

        Once this flight is added, you will need update the flight graph
        Such that in the next search, this flight is added
        """
        ...
