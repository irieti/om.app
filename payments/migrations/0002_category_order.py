# Generated by Django 5.1.2 on 2024-10-24 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("payments", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="order",
            field=models.PositiveIntegerField(default=0),
        ),
    ]