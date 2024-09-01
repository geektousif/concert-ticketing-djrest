from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from users.models import User
from .models import Concert
from .serializers import ConcertSerializer, GenerateSeatSerializer, SeatSerializer


# TODO shift it to core app
class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True

        return bool(
            request.user.is_authenticated
            and (request.user.is_staff or request.user.role == User.Roles.ADMIN)
        )


class ConcertViewSet(ModelViewSet):
    queryset = Concert.objects.all()
    serializer_class = ConcertSerializer
    permission_classes = [IsAdminOrReadOnly]

    @action(detail=True, methods=["post"], url_path="generate-seats")
    def generate_seats(self, request, pk=None):
        concert = self.get_object()
        serializer = GenerateSeatSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        seats = serializer.create(
            concert=concert, validated_data=serializer.validated_data
        )

        return Response(
            SeatSerializer(seats, many=True).data, status=status.HTTP_201_CREATED
        )
