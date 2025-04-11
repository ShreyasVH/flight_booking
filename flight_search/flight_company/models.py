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
        return f"{self.source} to {self.destination} on {self.start_time} by {self.company.name}"

    def serialize(self):
        return {
            'id': self.id,
            'source': self.source,
            'destination': self.destination,
            'start_time': self.start_time.isoformat(),
            'end_time': self.end_time.isoformat(),
            'cost': float(self.cost),
            'company_id': self.company.id,
            'operator_id': self.operator.id
        }

    @classmethod
    def deserialize(cls, data):
        from datetime import datetime
        from decimal import Decimal, ROUND_HALF_UP
        return cls(
            id=data.get('id'),
            source=data['source'],
            destination=data['destination'],
            start_time=datetime.fromisoformat(data['start_time']),
            end_time=datetime.fromisoformat(data['end_time']),
            cost=Decimal(data['cost']).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP),
            company_id=data['company_id'],
            operator_id=data['operator_id'],
        )


class Operator(models.Model):
    company = models.ForeignKey(FlightCompany, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
