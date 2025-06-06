from django.db import models

class Conference(models.Model):
    year = models.PositiveIntegerField(unique=True)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, help_text="Main conference description (supports markdown)")
    call_for_papers = models.TextField(blank=True, help_text="Call for papers content (supports markdown)")
    submission_button_text = models.CharField(max_length=200, blank=True, default="MANUSCRIPT SUBMISSION CLOSED", help_text="Text displayed on the submission button")
    submission_button_link = models.URLField(blank=True, help_text="URL for the submission button (leave empty to disable link)")
    date = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=200)
    venue = models.CharField(max_length=200, blank=True)
    address = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} ({self.year})"

    class Meta:
        ordering = ['-year']

class Speaker(models.Model):
    title = models.CharField(max_length=200, blank=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    conference = models.ForeignKey(Conference, on_delete=models.CASCADE, related_name='speakers')
    profile_image = models.ImageField(upload_to='speakers/', blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.conference.title}"

    class Meta:
        ordering = ['last_name', 'first_name']

class Organizer(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='organizers/', blank=True, null=True)

class ConferenceRole(models.Model):
    ROLE_CHOICES = [
        ('general_chair', 'General Chair'),
        ('program_chair', 'Program Chair'),
        ('organizer', 'Organizer'),
    ]
    
    conference = models.ForeignKey(Conference, on_delete=models.CASCADE, related_name='roles')
    title = models.CharField(max_length=200, blank=True, help_text="e.g., Prof., Dr.")
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    role_type = models.CharField(max_length=20, choices=ROLE_CHOICES)
    affiliation = models.CharField(max_length=300, blank=True, help_text="University or organization")
    order = models.PositiveIntegerField(default=0, help_text="Display order within role type")
    
    def __str__(self):
        title_part = f"{self.title} " if self.title else ""
        return f"{title_part}{self.first_name} {self.last_name} - {self.get_role_type_display()}"
    
    class Meta:
        ordering = ['role_type', 'order', 'last_name']

class AgendaItem(models.Model):
    ICON_CHOICES = [
        ('keynote', 'Keynote'),
        ('break', 'Break'),
        ('gathering', 'Gathering'),
        ('paper', 'Paper'),
        ('drinks', 'Drinks'),
    ]

    conference = models.ForeignKey(Conference, on_delete=models.CASCADE, related_name='agenda_items')
    time_start = models.TimeField()
    time_end = models.TimeField()
    title = models.CharField(max_length=200)
    icon = models.CharField(max_length=20, choices=ICON_CHOICES, default='keynote')

    def __str__(self):
        return f"{self.time_start} - {self.title}"

    class Meta:
        ordering = ['time_start']
