# Generated by Django 5.2 on 2025-06-06 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("conference", "0017_conference_map_address_conference_map_embed_url_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="agendaitem",
            name="content",
            field=models.TextField(
                blank=True,
                help_text="Agenda item content (supports markdown for lists, formatting, etc.)",
            ),
        ),
    ]
