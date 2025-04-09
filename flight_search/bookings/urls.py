from django.urls import URLPattern, path

from .views import Search, GetOrUpdateBooking, CreateBooking

urlpatterns: list[URLPattern] = [
    path("search/", Search.as_view(), name="search"),
    path("bookings/", CreateBooking.as_view(), name="create_booking"),
    path("bookings/<int:booking_id>/", GetOrUpdateBooking.as_view(), name="bookings"),
]
