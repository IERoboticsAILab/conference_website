from django.core.management.base import BaseCommand
from datetime import date
from conference.models import Conference, ImportantDate

class Command(BaseCommand):
    help = 'Populate conference with sample important dates'

    def handle(self, *args, **options):
        try:
            # Get the 2019 conference
            conference = Conference.objects.get(year=2019)
            
            # Clear existing important dates for this conference
            ImportantDate.objects.filter(conference=conference).delete()
            
            # Sample important dates data
            dates_data = [
                {
                    'title': 'Submission',
                    'is_closed': True,
                    'order': 1
                },
                {
                    'title': 'Paper Submission Deadline',
                    'date': date(2019, 10, 31),
                    'order': 2
                },
                {
                    'title': 'Author Notification',
                    'date': date(2019, 11, 5),
                    'order': 3
                },
                {
                    'title': 'Registration',
                    'is_closed': True,
                    'order': 4
                },
            ]
            
            # Create the important dates
            for date_data in dates_data:
                ImportantDate.objects.create(
                    conference=conference,
                    **date_data
                )
            
            self.stdout.write(
                self.style.SUCCESS(f'Successfully populated {len(dates_data)} important dates for conference {conference.year}')
            )
                
        except Conference.DoesNotExist:
            self.stdout.write(
                self.style.ERROR('Conference for year 2019 not found. Please create it first.')
            )
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Error: {str(e)}')
            ) 