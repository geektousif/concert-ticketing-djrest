from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from concerts.models import Seat
from .models import Purchase
from .serializers import PurchaseSerializer
# Create your views here.


class PurchaseViewSet(ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        seat_ids = request.data.get("seats", [])

        seats = Seat.objects.filter(id__in=seat_ids, is_booked=False)

        if seats.count() != len(seat_ids):
            return Response(
                {"error": "Seat/s not available"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        serializer = self.get_serializer(
            data={**request.data, "seats": seat_ids, "user": request.user.id}
        )
        serializer.is_valid(raise_exception=True)
        purchase = self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            PurchaseSerializer(purchase).data,
            status=status.HTTP_201_CREATED,
            headers=headers,
        )
