# Generated by Django 2.2.13 on 2020-08-12 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0018_food_foodlog"),
    ]

    operations = [
        migrations.AddField(
            model_name="dailyproductivitylog",
            name="mistakes",
            field=models.TextField(blank=True, default=""),
        ),
    ]
