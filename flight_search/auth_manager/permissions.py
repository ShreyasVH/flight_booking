from rest_framework.permissions import BasePermission


class IsPassenger(BasePermission):
    """
    Allows access only to users with role = PASSENGER.
    """

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'PASSENGER'


class IsFlightCompany(BasePermission):
    """
    Allows access only to users with role = FLIGHT_COMPANY.
    """

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'FLIGHT_COMPANY'
