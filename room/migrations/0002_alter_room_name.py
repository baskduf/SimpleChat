# Generated by Django 5.0.7 on 2024-07-20 09:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("room", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="room",
            name="name",
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
