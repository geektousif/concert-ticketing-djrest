from django.db import models
from concerts.models import Concert, Seat

from django.contrib.auth import get_user_model
# Create your models here.


User = get_user_model()


class PaymentStatusChoice(models.TextChoices):
    SUCCESS = "SUCCESS", "Success"
    FAILED = "FAILED", "Failed"
    PENDING = "PENDING", "Pending"


# LATER implement live status of seats as they are booked
class Purchase(models.Model):
    concert = models.ForeignKey(Concert, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.CharField(
        max_length=10,
        choices=PaymentStatusChoice.choices,
        default=PaymentStatusChoice.PENDING,
    )
    payment_date = models.DateTimeField(auto_now_add=True)
    transaction_id = models.CharField(max_length=255, null=True, blank=True)
    payment_method = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.user} - {self.concert}"


class Ticket(models.Model):
    purchase = models.ForeignKey(
        Purchase, on_delete=models.CASCADE, related_name="tickets"
    )
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    # qr_code = models.CharField(max_length=255, unique=True)  # REVIEW uuid if needed
