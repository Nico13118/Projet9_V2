# Generated by Django 4.1.3 on 2023-08-14 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_delete_reviewresponse'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='response',
            field=models.CharField(default='0', max_length=1),
        ),
    ]