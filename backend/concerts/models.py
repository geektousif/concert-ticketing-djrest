from django.db import models


# Create your models here.
class Concert(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateTimeField()
    venue = models.CharField(max_length=255)
    # seats = models.IntegerField()
    ticket_price = models.DecimalField(max_digits=10, decimal_places=2)
    poster = models.ImageField(upload_to="images/concerts/", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Seat(models.Model):
    concert = models.ForeignKey(Concert, on_delete=models.CASCADE, related_name="seats")
    row = models.CharField(max_length=5)
    seat_number = models.CharField(max_length=5)
    is_booked = models.BooleanField(default=False)

    class Meta:
        unique_together = [
            ["concert", "row", "seat_number"],
        ]
