from django.db import models
from auth_manager.models import FlightCompany


class Flight(models.Model):
    company = models.ForeignKey(FlightCompany, on_delete=models.CASCADE)
    source = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    capacity = models.PositiveIntegerField()
    operator = models.ForeignKey('Operator', on_delete=models.CASCADE)

    @property
    def duration_hours(self):
        if self.start_time and self.end_time:
            duration = self.end_time - self.start_time
            return round(duration.total_seconds() / 3600, 2)
        return 0

    def __str__(self):
        return f"{self.source} to {self.destination} on {self.date} by {self.company.name}"


class Operator(models.Model):
    company = models.ForeignKey(FlightCompany, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
