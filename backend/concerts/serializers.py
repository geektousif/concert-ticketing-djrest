from rest_framework import serializers
from .models import Concert, Seat
from .utils import generate_row_alphabets


class ConcertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Concert
        fields = "__all__"


class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = "__all__"


class GenerateSeatSerializer(serializers.Serializer):
    num_rows = serializers.IntegerField()
    seats_per_row = serializers.IntegerField()

    def create_seats(self, concert, num_rows, seats_per_row):
        rows = generate_row_alphabets(num_rows)
        seats = []
        for row in rows:
            for seat_number in range(1, seats_per_row + 1):
                seat = Seat(concert=concert, row=row, seat_number=str(seat_number))
                seats.append(seat)

        Seat.objects.bulk_create(seats)

        return seats

    def create(self, concert, validated_data):
        # concert = Concert.objects.get(id=validated_data["concert_id"])
        num_rows = validated_data["num_rows"]
        seats_per_row = validated_data["seats_per_row"]

        seats = self.create_seats(concert, num_rows, seats_per_row)

        return seats
