# Generated by Django 5.2 on 2025-06-06 20:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("conference", "0013_conference_submission_button_link_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="ImportantDate",
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
                (
                    "title",
                    models.CharField(
                        help_text="e.g., 'Paper Submission Deadline', 'Registration'",
                        max_length=200,
                    ),
                ),
                (
                    "date",
                    models.DateField(
                        blank=True,
                        help_text="Leave empty if using status text only",
                        null=True,
                    ),
                ),
                (
                    "status_text",
                    models.CharField(
                        blank=True,
                        help_text="e.g., 'CLOSED', 'OPEN' - shown instead of date if provided",
                        max_length=100,
                    ),
                ),
                (
                    "is_closed",
                    models.BooleanField(
                        default=False, help_text="Show as 'CLOSED' status"
                    ),
                ),
                (
                    "order",
                    models.PositiveIntegerField(default=0, help_text="Display order"),
                ),
                (
                    "conference",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="important_dates",
                        to="conference.conference",
                    ),
                ),
            ],
            options={
                "ordering": ["order", "title"],
            },
        ),
    ]
