# Generated by Django 4.1.9 on 2023-05-17 20:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("lists", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="List",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.TextField(default="")),
            ],
        ),
    ]