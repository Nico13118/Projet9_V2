# Generated by Django 4.1.3 on 2023-08-17 08:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_ticket_response'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='date_created_response',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
