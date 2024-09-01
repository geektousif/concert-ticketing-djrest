from rest_framework import serializers

from .models import Ticket, Purchase, PaymentStatusChoice
from concerts.serializers import SeatSerializer
from concerts.models import Seat

# BUG Odd Response but it works well in saving into db
# {
#     "concert": null,
#     "user": null,
#     "payment_method": "",
#     "seats": []
# }


class TicketSerializer(serializers.ModelSerializer):
    seat = SeatSerializer()

    class Meta:
        model = Ticket
        fields = [
            "id",
            "seat",
            # "qr_code",
        ]


class PurchaseSerializer(serializers.ModelSerializer):
    tickets = TicketSerializer(many=True, read_only=True)
    seats = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Seat.objects.all(), write_only=True
    )

    class Meta:
        model = Purchase
        fields = [
            "id",
            "concert",
            "user",
            "total_amount",
            "payment_status",
            "payment_date",
            "transaction_id",
            "payment_method",
            "tickets",
            "seats",
        ]
        read_only_fields = [
            "total_amount",
            "payment_status",
            "payment_date",
            "transaction_id",
            "tickets",
        ]

    def create(self, validated_data):
        concert = validated_data["concert"]
        user = validated_data["user"]
        seats = validated_data.pop("seats", [])

        # concert_item = Concert.objects.get(id=concert.id)
        total_amount = concert.ticket_price * len(seats)

        purchase = Purchase.objects.create(
            concert=concert,
            user=user,
            total_amount=total_amount,
            payment_status=PaymentStatusChoice.PENDING,
        )  # TODO implement payment status update along with transaction id

        tickets = []

        for seat in seats:
            seat.is_booked = True
            seat.save()

            # TODO Generate QR code
            ticket = Ticket.objects.create(purchase=purchase, seat=seat)
            tickets.append(ticket)

        return purchase
