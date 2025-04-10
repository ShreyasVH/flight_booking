from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from django.shortcuts import render, redirect, get_object_or_404
from flight_company.forms import OperatorForm
from flight_company.models import Operator


class GetOrUpdateOperator(APIView):
    # implement proper permissions here
    permission_classes = []

    def get(self, request: Request, operator_id: int):
        """
        Will fetch details of a operator.
        """
        ...
        user = request.user
        operator = get_object_or_404(Operator, id=operator_id, company=user.flight_company)

        form = OperatorForm(instance=operator)
        return render(request, 'operators/edit_operator.html', {'form': form, 'operator': operator})

    def post(self, request: Request, operator_id: int):
        """
        This call will update any other info about the operator
        """
        ...
        user = request.user
        operator = get_object_or_404(Operator, id=operator_id, company=user.flight_company)

        if request.POST.get("_method") == "DELETE":
            operator.delete()
            return redirect('/operators/list')

        form = OperatorForm(request.POST, instance=operator)
        if form.is_valid():
            form.save()
            return redirect('/operators/list')
        return render(request, 'operators/edit_operator.html', {'form': form, 'operator': operator})

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
        form = OperatorForm(request.POST)
        if form.is_valid():
            operator = form.save(commit=False)
            operator.company = user.flight_company
            operator.save()

        return redirect('/operators/list')

    def get(self, request: Request):
        form = OperatorForm()
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
