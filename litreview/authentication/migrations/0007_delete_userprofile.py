# Generated by Django 4.1.3 on 2023-08-11 09:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0006_user_follows_user_role'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
