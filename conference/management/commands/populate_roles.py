from django.core.management.base import BaseCommand
from conference.models import Conference, ConferenceRole

class Command(BaseCommand):
    help = 'Populate conference with sample role data (general chairs, program chairs, organizers)'

    def handle(self, *args, **options):
        try:
            # Get the 2019 conference
            conference = Conference.objects.get(year=2019)
            
            # Clear existing roles for this conference
            ConferenceRole.objects.filter(conference=conference).delete()
            
            # Sample role data
            roles_data = [
                # General Chairs
                {
                    'title': 'Prof.',
                    'first_name': 'Alex',
                    'last_name': 'Pentland',
                    'role_type': 'general_chair',
                    'affiliation': 'MIT Media Lab',
                    'order': 1
                },
                {
                    'title': 'Prof.',
                    'first_name': 'Marco',
                    'last_name': 'Dorigo',
                    'role_type': 'general_chair',
                    'affiliation': 'Université Libre de Bruxelles',
                    'order': 2
                },
                {
                    'title': 'Dr.',
                    'first_name': 'Thomas',
                    'last_name': 'Hardjono',
                    'role_type': 'general_chair',
                    'affiliation': 'MIT',
                    'order': 3
                },
                
                # Program Chairs
                {
                    'title': 'Prof.',
                    'first_name': 'Javier',
                    'last_name': 'Alonso-Mora',
                    'role_type': 'program_chair',
                    'affiliation': 'TU Delft',
                    'order': 1
                },
                {
                    'title': 'Prof.',
                    'first_name': 'Carlo',
                    'last_name': 'Pinciroli',
                    'role_type': 'program_chair',
                    'affiliation': 'Worcester Polytechnic Institute',
                    'order': 2
                },
                {
                    'title': 'Prof.',
                    'first_name': 'Fabio',
                    'last_name': 'Bonsignorio',
                    'role_type': 'program_chair',
                    'affiliation': 'Università di Genova',
                    'order': 3
                },
                {
                    'title': 'Dr.',
                    'first_name': 'Antonio',
                    'last_name': 'Bucchiarone',
                    'role_type': 'program_chair',
                    'affiliation': 'Fondazione Bruno Kessler',
                    'order': 4
                },
                {
                    'title': 'Prof.',
                    'first_name': 'Aleksandr',
                    'last_name': 'Kapitonov',
                    'role_type': 'program_chair',
                    'affiliation': 'ITMO University',
                    'order': 5
                },
                
                # Organizers
                {
                    'title': 'Dr.',
                    'first_name': 'Eduardo',
                    'last_name': 'Castelló Ferrer',
                    'role_type': 'organizer',
                    'affiliation': 'MIT Media Lab',
                    'order': 1
                },
                {
                    'title': 'Dr.',
                    'first_name': 'Darko',
                    'last_name': 'Bozhinoski',
                    'role_type': 'organizer',
                    'affiliation': 'TU Delft',
                    'order': 2
                },
            ]
            
            # Create the roles
            for role_data in roles_data:
                ConferenceRole.objects.create(
                    conference=conference,
                    **role_data
                )
            
            self.stdout.write(
                self.style.SUCCESS(f'Successfully populated {len(roles_data)} roles for conference {conference.year}')
            )
                
        except Conference.DoesNotExist:
            self.stdout.write(
                self.style.ERROR('Conference for year 2019 not found. Please create it first.')
            )
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Error: {str(e)}')
            ) 