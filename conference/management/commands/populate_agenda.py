from django.core.management.base import BaseCommand
from conference.models import Conference, AgendaItem
from datetime import time

class Command(BaseCommand):
    help = 'Populate agenda items for the 2019 conference with markdown examples'

    def handle(self, *args, **options):
        try:
            # Get the 2019 conference
            conference = Conference.objects.get(year=2019)
            
            # Clear existing agenda items for this conference
            AgendaItem.objects.filter(conference=conference).delete()
            
            # Sample agenda data with markdown content
            agenda_items = [
                {
                    "time_start": time(9, 0),
                    "time_end": time(9, 30),
                    "content": "**Registration & Welcome Coffee**\n\n- Check-in at reception\n- Light breakfast served\n- Networking opportunity",
                    "icon": "gathering"
                },
                {
                    "time_start": time(9, 30),
                    "time_end": time(10, 30),
                    "content": "**Keynote: The Future of Blockchain in Robotics**\n\n*Speaker: Dr. Jane Smith, MIT*\n\n- Current applications\n- Future possibilities\n- Q&A session",
                    "icon": "keynote"
                },
                {
                    "time_start": time(10, 30),
                    "time_end": time(11, 0),
                    "content": "**Coffee Break**",
                    "icon": "break"
                },
                {
                    "time_start": time(11, 0),
                    "time_end": time(12, 30),
                    "content": "**Technical Sessions**\n\n1. **Blockchain Integration in Autonomous Systems**\n   - Paper presentations (15 min each)\n   - Panel discussion\n\n2. **AI and Distributed Ledgers**\n   - Case studies\n   - Implementation challenges",
                    "icon": "paper"
                },
                {
                    "time_start": time(12, 30),
                    "time_end": time(13, 30),
                    "content": "**Lunch Break**\n\n- Networking lunch\n- Poster session\n- Demo area open",
                    "icon": "break"
                },
                {
                    "time_start": time(17, 0),
                    "time_end": time(19, 0),
                    "content": "**Closing Reception**\n\n- Awards ceremony\n- Cocktails and appetizers\n- Final networking",
                    "icon": "drinks"
                }
            ]
            
            for item_data in agenda_items:
                AgendaItem.objects.create(
                    conference=conference,
                    time_start=item_data["time_start"],
                    time_end=item_data["time_end"],
                    content=item_data["content"],
                    icon=item_data["icon"]
                )
            
            self.stdout.write(
                self.style.SUCCESS(f'Successfully created {len(agenda_items)} agenda items with markdown content for conference {conference.year}')
            )
                
        except Conference.DoesNotExist:
            self.stdout.write(
                self.style.ERROR('Conference for year 2019 not found. Please create it first.')
            )
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Error: {str(e)}')
            ) 