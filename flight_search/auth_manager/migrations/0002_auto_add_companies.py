# Generated by Django 4.2.19 on 2025-04-10 04:29

from django.db import migrations
import os
from django.contrib.auth.hashers import make_password


def create_initial_flight_companies(apps, schema_editor):
    FlightCompany = apps.get_model('auth_manager', 'FlightCompany')
    # user = apps.get_model('auth_manager', 'User')
    # indigo = FlightCompany.objects.create(name="Indigo")
    # user.objects.create(username="IndigoAdmin", email="admin@indigo.com", is_staff=True, is_superuser=True, role="FLIGHT_COMPANY", flight_company=indigo, password=make_password(os.environ.get('ADMIN_DEFAULT_PASSWORD')))
    # air_india = FlightCompany.objects.create(name="Air India")
    # user.objects.create(username="AirIndiaAdmin", email="admin@airindia.com", is_staff=True, is_superuser=True, role="FLIGHT_COMPANY", flight_company=indigo, password=make_password(os.environ.get('ADMIN_DEFAULT_PASSWORD')))
    # spice_jet = FlightCompany.objects.create(name="SpiceJet")
    # user.objects.create(username="IndigoAdmin", email="admin@indigo.com", is_staff=True, is_superuser=True, role="FLIGHT_COMPANY", flight_company=indigo, password=make_password(os.environ.get('ADMIN_DEFAULT_PASSWORD')))


class Migration(migrations.Migration):

    dependencies = [
        ('auth_manager', '0001_initial')
    ]

    operations = [
        migrations.RunPython(create_initial_flight_companies),
    ]
