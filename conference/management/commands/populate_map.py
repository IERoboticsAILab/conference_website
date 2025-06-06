from django.core.management.base import BaseCommand
from conference.models import Conference

class Command(BaseCommand):
    help = 'Populate conference with map section content'

    def handle(self, *args, **options):
        try:
            # Get the 2019 conference
            conference = Conference.objects.get(year=2019)
            
            # Set map section content
            conference.map_venue_name = "MIT<br>Media<br>Lab"
            conference.map_address = "E14, 6th floor, 75 Amherst St,<br>Cambridge, MA 02139"
            conference.map_embed_url = "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2948.2276479384876!2d-71.08758508422983!3d42.36059857918531!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89e370a5cb30cc5f%3A0x1aa6ce1ad4ebeaca!2sMIT%20Media%20Lab!5e0!3m2!1sen!2sus!4v1641234567890!5m2!1sen!2sus"
            conference.show_map = True
            conference.save()
            
            self.stdout.write(
                self.style.SUCCESS(f'Successfully populated map section for conference {conference.year}')
            )
                
        except Conference.DoesNotExist:
            self.stdout.write(
                self.style.ERROR('Conference for year 2019 not found. Please create it first.')
            )
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Error: {str(e)}')
            ) 