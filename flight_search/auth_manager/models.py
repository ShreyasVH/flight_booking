from django.contrib.auth.models import AbstractUser
from django.db import models

class FlightCompany(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class User(AbstractUser):
    ROLE_CHOICES = (
        ('PASSENGER', 'Passenger'),
        ('FLIGHT_COMPANY', 'Flight Company'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    flight_company = models.ForeignKey(
        FlightCompany,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        help_text="Required only for FLIGHT_COMPANY users"
    )

    def __str__(self):
        return f"{self.username} ({self.role})"
