from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView


class GetOrUpdateOperator(APIView):
    # implement proper permissions here
    permission_classes = []

    def get(self, request: Request, operator_id: int) -> Response:
        """
        Will fetch details of a operator.
        """
        ...

    def put(self, request: Request, operator_id: int) -> Response:
        """
        This call will update any other info about the operator
        """
        ...

    def delete(self, request: Request, operator_id: int) -> Response:
        """
        This view will delete a airline operator
        """
        ...


class CreateOperator(APIView):
    # implement proper permissions here
    permission_classes = []

    def post(self, request: Request) -> Response:
        """
        This view will register a new operator of airlines
        Its a post call, hence will have some post params like, company_name, owner, etc...
        """
        ...
