from django.db import models
from auth_manager.models import User
from flight_company.models import Flight

# Create your models here.
class Booking(models.Model):
    passenger = models.ForeignKey(User, on_delete=models.CASCADE)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    seat_number = models.PositiveIntegerField()
    booked_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('flight', 'seat_number')  # prevent double booking of same seat

    def __str__(self):
        return f"{self.passenger.username} - Seat {self.seat_number} on {self.flight}"
