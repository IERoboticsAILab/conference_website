from django.core.management.base import BaseCommand
from conference.models import Conference, Organizer

class Command(BaseCommand):
    help = 'Populate organizers for the 2019 conference'

    def handle(self, *args, **options):
        try:
            # Get the 2019 conference
            conference = Conference.objects.get(year=2019)
            
            # Clear existing organizers for this conference
            Organizer.objects.filter(conference=conference).delete()
            
            # Sample organizer data - you can customize these
            organizers_data = [
                {"name": "MIT Media Lab", "order": 1},
                {"name": "Blockchain Research Institute", "order": 2},
                {"name": "IEEE Robotics Society", "order": 3},
                {"name": "AI Research Foundation", "order": 4},
            ]
            
            for org_data in organizers_data:
                Organizer.objects.create(
                    conference=conference,
                    name=org_data["name"],
                    order=org_data["order"]
                )
            
            self.stdout.write(
                self.style.SUCCESS(f'Successfully created {len(organizers_data)} organizers for conference {conference.year}')
            )
                
        except Conference.DoesNotExist:
            self.stdout.write(
                self.style.ERROR('Conference for year 2019 not found. Please create it first.')
            )
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Error: {str(e)}')
            ) 