from django.contrib import admin

# Register your models here.
from .models import Ticket, Purchase


admin.site.register(Ticket)
admin.site.register(Purchase)
