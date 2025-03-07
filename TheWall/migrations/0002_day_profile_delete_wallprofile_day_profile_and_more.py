# Generated by Django 5.1.3 on 2025-03-07 04:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("TheWall", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Day",
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
                ("day_number", models.IntegerField()),
                ("cost", models.IntegerField()),
                ("ice_amount", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Profile",
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
                ("name", models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name="WallProfile",
        ),
        migrations.AddField(
            model_name="day",
            name="profile",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="days",
                to="TheWall.profile",
            ),
        ),
        migrations.AlterUniqueTogether(
            name="day",
            unique_together={("profile", "day_number")},
        ),
    ]
