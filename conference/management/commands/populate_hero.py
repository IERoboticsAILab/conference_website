from django.core.management.base import BaseCommand
from conference.models import Conference

class Command(BaseCommand):
    help = 'Populate conference with hero section content'

    def handle(self, *args, **options):
        try:
            # Get the 2019 conference
            conference = Conference.objects.get(year=2019)
            
            # Set hero section content
            conference.hero_title = "Symposium on Blockchain for Robotics and AI Systems"
            conference.hero_subtitle = "Dec. 4th, 2019<br>MIT Media Lab (E14, 6th floor)<br>Cambridge, MA, USA"
            conference.livestream_label = "Livestream"
            conference.livestream_video_url = "https://www.youtube.com/embed/ReXFCqx5--s"
            conference.show_livestream = True
            conference.save()
            
            self.stdout.write(
                self.style.SUCCESS(f'Successfully populated hero section for conference {conference.year}')
            )
                
        except Conference.DoesNotExist:
            self.stdout.write(
                self.style.ERROR('Conference for year 2019 not found. Please create it first.')
            )
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Error: {str(e)}')
            ) 