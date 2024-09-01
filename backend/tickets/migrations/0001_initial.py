# Generated by Django 5.1 on 2024-08-09 18:25

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('concerts', '0002_remove_concert_seats_seat'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_status', models.CharField(choices=[('SUCCESS', 'Success'), ('FAILED', 'Failed'), ('PENDING', 'Pending')], default='PENDING', max_length=10)),
                ('payment_date', models.DateTimeField(auto_now_add=True)),
                ('transaction_id', models.CharField(blank=True, max_length=255, null=True)),
                ('payment_method', models.CharField(blank=True, max_length=255, null=True)),
                ('concert', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='concerts.concert')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qr_code', models.CharField(max_length=255, unique=True)),
                ('purchase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tickets', to='tickets.purchase')),
                ('seat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='concerts.seat')),
            ],
        ),
    ]
