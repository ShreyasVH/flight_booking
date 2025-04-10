from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from django.shortcuts import render, redirect
from flight_company.forms import CreateOperatorForm
from flight_company.models import Operator


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
        user = request.user
        form = CreateOperatorForm(request.POST)
        if form.is_valid():
            operator = form.save(commit=False)
            operator.company = user.flight_company
            operator.save()

        return redirect('/operators/list')

    def get(self, request: Request):
        form = CreateOperatorForm()
        return render(request, 'operators/create_operator.html', {'form': form})


class ListOperators(APIView):
    permission_classes = []

    def get(self, request: Request):
        """
        This will fetch all the details for an operator.
        """
        ...
        user = request.user

        operators = Operator.objects.filter(company=user.flight_company)

        return render(request, 'operators/view_operators.html', {'operators': operators})
