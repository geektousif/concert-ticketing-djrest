# Generated by Django 5.1 on 2024-08-09 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Concert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('date', models.DateTimeField()),
                ('venue', models.CharField(max_length=255)),
                ('seats', models.IntegerField()),
                ('ticket_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('poster', models.ImageField(blank=True, null=True, upload_to='images/concerts/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
