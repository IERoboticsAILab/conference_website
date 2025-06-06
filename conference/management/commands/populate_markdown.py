from django.core.management.base import BaseCommand
from conference.models import Conference

class Command(BaseCommand):
    help = 'Populate conference with sample markdown content'

    def handle(self, *args, **options):
        try:
            # Get the 2019 conference or create it if it doesn't exist
            conference, created = Conference.objects.get_or_create(
                year=2019,
                defaults={
                    'title': 'Symposium on Blockchain for Robotics and AI Systems',
                    'location': 'Cambridge, MA, USA',
                    'venue': 'MIT Media Lab (E14, 6th floor)',
                }
            )
            
            # Sample markdown content for description
            description_content = """
## About the Symposium

**Robotics and AI systems** are starting to revolutionize many applications, from *transportation* to *health care*, assisted by technological advancements, such as:

- Cloud computing
- Novel hardware design
- Advanced algorithms

### Key Challenges

However, several of the characteristics that make these systems ideal for certain future applications such as **autonomy**, **self-learning**, and **knowledge sharing**, can also raise concerns in the evolution of the technology from academic institutions into the public sphere.

> Blockchain is starting to show great potential to make robotics and AI operations more secure, autonomous, flexible, and even profitable.

#### Our Mission

This symposium seeks to move beyond the classical view of distributed systems to advance our understanding about the possibilities and limitations of combining state-of-the-art robotics and AI systems with blockchain technology.

**Key Questions We Address:**
- How can blockchain enhance AI and robotics security?
- What are the practical applications in real-world scenarios?
- How do we bridge the gap between scientific research and industry implementation?
"""

            # Sample markdown content for call for papers
            call_for_papers_content = """
# Call for Papers

Decentralized artificial intelligence and robotics have the potential to revolutionize many applications. Boosted by technological advancements, such as cloud computing and novel hardware design; nowadays AI (virtual) and robotics (physical) are starting to become an important part of activities such as:

- **Logistics** and supply chain management
- **Autonomous transportation** systems
- **Emergency management** and disaster response
- **Healthcare** and medical robotics

## Research Challenges

However, several characteristics that make these systems ideal for future applications can also raise concerns:

!!! warning "Key Challenges"
    - Controlling behavior of large teams of autonomous agents
    - Data privacy, security, safety, and transparency issues
    - Integration challenges in high-sensitive scenarios

### Blockchain Solutions

**Blockchain** technology demonstrates that by combining peer-to-peer networks with cryptographic algorithms, agents can reach agreements in a transparent and decentralized manner without the need for a controlling authority.

> Smart contracts are already showing great potential to make distributed robotics operations more secure, autonomous, flexible, and even profitable.

## Research Topics

Below is a list of possible topics that would fit this CFP:

| Category | Topics |
|----------|--------|
| **Technology** | Blockchain-based technology for cyber-physical systems |
| **Security** | Data privacy, security, safety, and transparency for AI and robotics |
| **Auditing** | Auditability for Internet of Robotic Things (IoRT) |
| **Collaboration** | Collaborative approaches for teams of autonomous agents |
| **Networks** | Decentralized, distributed, and federated networks for AI and robotics |
| **Business** | New decentralized business models for AI and robotics |

### Research Questions

We're particularly interested in insights about the following questions:

1. What blockchain tools are available to increase the **auditability**, **transparency**, and **reliability** of AI and robotics?
2. What kind of algorithms are suitable to combine both technologies?
3. Are there new models and methods to connect autonomous agents to blockchain-based innovations such as "smart contracts"?
4. Is blockchain technology a suitable way to achieve emergent aggregations of autonomous and self-adaptive agents?
5. Are distributed networks such as Bitcoin, Ethereum, EOS, Tezos, etc. a feasible way to integrate AI and robotics in our society?

## Submission Guidelines

!!! info "Important Note"
    Accepted papers will be published as a research topic by **Frontiers in Robotics and AI**. All contributions must be within the scope of the section and journal.

### Keywords
`Blockchain`, `Smart Contracts`, `Robotics`, `AI`, `Cyber-Physical Systems`, `Trustable Automation`, `Data Privacy`, `Verifiable Autonomy`, `Auditable Systems`, `Distributed Learning`, `Networked Systems`, `Internet of Things`, `Collective Adaptation`, `Collaborative Systems`, `New Business Models`

---

*We welcome both conceptual and theoretical contributions as well as papers documenting valuable results of experiments conducted with real-robots or AI implementations.*
"""

            # Update the conference with markdown content
            conference.description = description_content
            conference.call_for_papers = call_for_papers_content
            conference.save()
            
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f'Created new conference for {conference.year} with markdown content')
                )
            else:
                self.stdout.write(
                    self.style.SUCCESS(f'Updated existing conference for {conference.year} with markdown content')
                )
                
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Error: {str(e)}')
            ) 