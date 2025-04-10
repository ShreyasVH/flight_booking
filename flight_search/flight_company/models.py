from django.db import models
from auth_manager.models import FlightCompany


class Flight(models.Model):
    company = models.ForeignKey(FlightCompany, on_delete=models.CASCADE)
    source = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    operator = models.ForeignKey('Operator', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.source} to {self.destination} on {self.date} by {self.company.name}"


class Operator(models.Model):
    company = models.ForeignKey(FlightCompany, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
