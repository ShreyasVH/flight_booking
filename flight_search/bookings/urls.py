from django.urls import URLPattern, path

from .views import Search, GetOrUpdateBooking, CreateBooking, MyBookings

urlpatterns: list[URLPattern] = [
    path("search/", Search.as_view(), name="search"),
    path("bookings/create/<int:flight_id>", CreateBooking.as_view(), name="create_booking"),
    path("bookings/my", MyBookings.as_view(), name="create_booking"),
    path("bookings/<int:booking_id>/", GetOrUpdateBooking.as_view(), name="bookings"),
]
