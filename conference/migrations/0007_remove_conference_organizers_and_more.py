# Generated by Django 5.2 on 2025-06-05 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("conference", "0006_alter_speaker_options_remove_speaker_person_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="conference",
            name="organizers",
        ),
        migrations.RemoveField(
            model_name="conference",
            name="general_chairs",
        ),
        migrations.RemoveField(
            model_name="conference",
            name="program_chairs",
        ),
        migrations.RemoveField(
            model_name="agendaitem",
            name="description",
        ),
        migrations.RemoveField(
            model_name="agendaitem",
            name="is_break",
        ),
        migrations.RemoveField(
            model_name="agendaitem",
            name="speakers",
        ),
        migrations.AddField(
            model_name="agendaitem",
            name="icon",
            field=models.CharField(
                choices=[
                    ("keynote", "Keynote"),
                    ("break", "Break"),
                    ("gathering", "Gathering"),
                    ("paper", "Paper"),
                    ("drinks", "Drinks"),
                ],
                default="presentation",
                max_length=20,
            ),
        ),
        migrations.DeleteModel(
            name="ImportantDate",
        ),
        migrations.DeleteModel(
            name="Person",
        ),
    ]
