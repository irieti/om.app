# Generated by Django 5.1.2 on 2024-10-25 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("payments", "0004_remove_menuitem_subcategories_menuitem_subcategory"),
    ]

    operations = [
        migrations.AddField(
            model_name="subcategory",
            name="order",
            field=models.PositiveIntegerField(default=0),
        ),
    ]