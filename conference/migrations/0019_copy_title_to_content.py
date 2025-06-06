# Generated manually
from django.db import migrations

def copy_title_to_content(apps, schema_editor):
    AgendaItem = apps.get_model('conference', 'AgendaItem')
    for item in AgendaItem.objects.all():
        item.content = item.title
        item.save()

def reverse_copy_content_to_title(apps, schema_editor):
    AgendaItem = apps.get_model('conference', 'AgendaItem')
    for item in AgendaItem.objects.all():
        item.title = item.content
        item.save()

class Migration(migrations.Migration):

    dependencies = [
        ('conference', '0018_add_content_to_agenda'),
    ]

    operations = [
        migrations.RunPython(copy_title_to_content, reverse_copy_content_to_title),
    ] 