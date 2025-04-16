from django.core.management.base import BaseCommand
from django.utils import timezone
from auth_manager.models import User, FlightCompany
from flight_company.models import Operator, Flight
from bookings.models import Booking
from datetime import datetime, timedelta
from django.contrib.auth.hashers import make_password

class Command(BaseCommand):
    help = 'Seeds demo data: companies, users, operators, flights, etc.'

    def handle(self, *args, **kwargs):
        User.objects.create(
            username="admin",
            email="admin@gmail.com",
            role="ADMIN",
            is_superuser=True,
            password=make_password('Test@123')
        )

        # # Create flight companies
        # indigo = FlightCompany.objects.get_or_create(name="Indigo")[0]
        # air_india = FlightCompany.objects.get_or_create(name="Air India")[0]
        # spice_jet = FlightCompany.objects.get_or_create(name="Spice Jet")[0]
        #
        # # Create users (flight company users)
        # if not User.objects.filter(username="IndigoAdmin").exists():
        #     u = User.objects.create(
        #         username="IndigoAdmin",
        #         email="admin@indigo.com",
        #         role="FLIGHT_COMPANY",
        #         flight_company=indigo
        #     )
        #     u.set_password("Test@123")
        #     u.save()
        #     self.stdout.write("✅ Created indigo_admin")
        #
        # if not User.objects.filter(username="AirIndiaAdmin").exists():
        #     u = User.objects.create(
        #         username="AirIndiaAdmin",
        #         email="admin@airindia.com",
        #         role="FLIGHT_COMPANY",
        #         flight_company=air_india
        #     )
        #     u.set_password("Test@123")
        #     u.save()
        #     self.stdout.write("✅ Created AirIndiaAdmin")
        #
        # if not User.objects.filter(username="SpiceJetAdmin").exists():
        #     u = User.objects.create(
        #         username="SpiceJetAdmin",
        #         email="admin@spicejet.com",
        #         role="FLIGHT_COMPANY",
        #         flight_company=spice_jet
        #     )
        #     u.set_password("Test@123")
        #     u.save()
        #     self.stdout.write("✅ Created SpiceJetAdmin")
        #
        # operator_paul_smith = Operator.objects.get_or_create(
        #     first_name="Paul",
        #     last_name="Smith",
        #     company=indigo
        # )[0]
        #
        # operator_harry_potter = Operator.objects.get_or_create(
        #     first_name="Harry",
        #     last_name="Potter",
        #     company=spice_jet
        # )[0]
        #
        # operator_ron_weasly = Operator.objects.get_or_create(
        #     first_name="Ron",
        #     last_name="Weasly",
        #     company=spice_jet
        # )[0]
        #
        # passenger_jack_kallis = User.objects.get_or_create(
        #     username="JackKallis",
        #     email="jack.kallis@gmail.com",
        #     role="PASSENGER",
        #     password=make_password("Test@123")
        # )[0]
        #
        # passenger_ricky_ponting = User.objects.get_or_create(
        #     username="RickyPonting",
        #     email="ricky.ponting@gmail.com",
        #     role="PASSENGER",
        #     password=make_password("Test@123")
        # )[0]
        #
        # passenger_rahul_dravid = User.objects.get_or_create(
        #     username="RahulDravid",
        #     email="rahul.dravid@gmail.com",
        #     role="PASSENGER",
        #     password=make_password("Test@123")
        # )[0]
        #
        # passenger_kl_rahul = User.objects.get_or_create(
        #     username="KLRahul",
        #     email="kl.rahul@gmail.com",
        #     role="PASSENGER",
        #     password=make_password("Test@123")
        # )[0]
        #
        # passenger_nick_fury = User.objects.get_or_create(
        #     username="NickFury",
        #     email="nick.fury@gmail.com",
        #     role="PASSENGER",
        #     password=make_password("Test@123")
        # )[0]
        #
        # passenger_manish_pandey = User.objects.get_or_create(
        #     username="ManishPandey",
        #     email="manish.pandey@gmail.com",
        #     role="PASSENGER",
        #     password=make_password("Test@123")
        # )[0]
        #
        # # Create flight
        # flight_1 = Flight.objects.get_or_create(
        #     company=indigo,
        #     operator=operator_paul_smith,
        #     source="Bengaluru",
        #     destination="Delhi",
        #     cost=12000,
        #     start_time=datetime.strptime("2025-03-31 23:00", "%Y-%m-%d %H:%M"),
        #     end_time=datetime.strptime("2025-04-01 02:00", "%Y-%m-%d %H:%M"),
        #     capacity=30
        # )[0]
        #
        # flight_2 = Flight.objects.get_or_create(
        #     company=indigo,
        #     operator=operator_paul_smith,
        #     source="Delhi",
        #     destination="Bengaluru",
        #     cost=10000,
        #     start_time=datetime.strptime("2025-03-11 10:00", "%Y-%m-%d %H:%M"),
        #     end_time=datetime.strptime("2025-03-11 12:00", "%Y-%m-%d %H:%M"),
        #     capacity=35
        # )[0]
        #
        # flight_3 = Flight.objects.get_or_create(
        #     company=spice_jet,
        #     operator=operator_harry_potter,
        #     source="Bengaluru",
        #     destination="Mysuru",
        #     cost=15000,
        #     start_time=datetime.strptime("2025-03-20 10:30", "%Y-%m-%d %H:%M"),
        #     end_time=datetime.strptime("2025-03-20 12:00", "%Y-%m-%d %H:%M"),
        #     capacity=30
        # )[0]
        #
        # flight_4 = Flight.objects.get_or_create(
        #     company=indigo,
        #     operator=operator_paul_smith,
        #     source="Mysuru",
        #     destination="Delhi",
        #     cost=7000,
        #     start_time=datetime.strptime("2025-04-03 09:00", "%Y-%m-%d %H:%M"),
        #     end_time=datetime.strptime("2025-04-03 10:30", "%Y-%m-%d %H:%M"),
        #     capacity=35
        # )[0]
        #
        # flight_5 = Flight.objects.get_or_create(
        #     company=indigo,
        #     operator=operator_paul_smith,
        #     source="Delhi",
        #     destination="Shimla",
        #     cost=9000,
        #     start_time=datetime.strptime("2025-04-15 10:00", "%Y-%m-%d %H:%M"),
        #     end_time=datetime.strptime("2025-04-15 12:30", "%Y-%m-%d %H:%M"),
        #     capacity=30
        # )[0]
        #
        # Booking.objects.create(
        #     flight=flight_1,
        #     passenger=passenger_jack_kallis,
        #     seat_number=1
        # )
        #
        # Booking.objects.create(
        #     flight=flight_1,
        #     passenger=passenger_ricky_ponting,
        #     seat_number=2
        # )
        #
        # Booking.objects.create(
        #     flight=flight_2,
        #     passenger=passenger_rahul_dravid,
        #     seat_number=1
        # )
        #
        # Booking.objects.create(
        #     flight=flight_3,
        #     passenger=passenger_kl_rahul,
        #     seat_number=1
        # )
        #
        # Booking.objects.create(
        #     flight=flight_4,
        #     passenger=passenger_nick_fury,
        #     seat_number=1
        # )
        #
        # Booking.objects.create(
        #     flight=flight_5,
        #     passenger=passenger_manish_pandey,
        #     seat_number=1
        # )

        self.stdout.write(self.style.SUCCESS("🎉 Demo data seeded!"))
