# Generated by Django 4.1.3 on 2023-10-02 16:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_delete_userfollows'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='photo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.photo'),
        ),
    ]
