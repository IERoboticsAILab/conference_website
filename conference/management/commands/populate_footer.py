from django.core.management.base import BaseCommand
from conference.models import Footer

class Command(BaseCommand):
    help = 'Populate footer settings with sample data'

    def handle(self, *args, **options):
        try:
            # Clear existing footer settings
            Footer.objects.all().delete()
            
            # Create footer settings
            footer = Footer.objects.create(
                organization_name="Blockchain Robotics Research Institute",
                tagline="Advancing the intersection of blockchain technology and autonomous systems",
                email="info@blockchainrobotics.org",
                phone="+1 (555) 123-4567",
                address="MIT Media Lab<br>75 Amherst St, Building E14<br>Cambridge, MA 02139",
                twitter_url="https://twitter.com/blockchain_robotics",
                linkedin_url="https://linkedin.com/company/blockchain-robotics",
                github_url="https://github.com/blockchain-robotics",
                copyright_text="Blockchain Robotics Research Institute. All rights reserved.",
                additional_info="**Research Areas:**\n\n- Distributed autonomous systems\n- Blockchain consensus in robotics\n- AI-driven smart contracts\n- Decentralized robot networks",
                show_social_links=True,
                show_contact_info=True
            )
            
            self.stdout.write(
                self.style.SUCCESS(f'Successfully created footer settings for {footer.organization_name}')
            )
                
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Error: {str(e)}')
            ) 