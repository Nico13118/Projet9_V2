# Generated by Django 4.1.3 on 2023-08-12 15:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_review_ticket'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ReviewResponse',
        ),
    ]
