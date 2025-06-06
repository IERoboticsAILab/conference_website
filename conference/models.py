from django.db import models

class Conference(models.Model):
    year = models.PositiveIntegerField(unique=True)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, help_text="Main conference description (supports markdown)")
    call_for_papers = models.TextField(blank=True, help_text="Call for papers content (supports markdown)")
    submission_button_text = models.CharField(max_length=200, blank=True, default="MANUSCRIPT SUBMISSION CLOSED", help_text="Text displayed on the submission button")
    submission_button_link = models.URLField(blank=True, help_text="URL for the submission button (leave empty to disable link)")
    
    # Hero section fields
    hero_title = models.CharField(max_length=300, blank=True, help_text="Main title in hero section (defaults to conference title if empty)")
    hero_subtitle = models.TextField(blank=True, help_text="Subtitle with date, location, etc. Supports line breaks with <br>")
    livestream_label = models.CharField(max_length=100, blank=True, default="Livestream", help_text="Label above the video")
    livestream_video_url = models.URLField(blank=True, help_text="YouTube embed URL (e.g., https://www.youtube.com/embed/VIDEO_ID)")
    show_livestream = models.BooleanField(default=True, help_text="Show/hide the livestream video section")
    
    # Map section fields
    map_venue_name = models.CharField(max_length=200, blank=True, help_text="Large venue name displayed on map (supports line breaks with <br>)")
    map_address = models.TextField(blank=True, help_text="Detailed address shown below venue name (supports line breaks with <br>)")
    map_embed_url = models.URLField(blank=True, help_text="Google Maps embed URL (get from Google Maps > Share > Embed)")
    show_map = models.BooleanField(default=True, help_text="Show/hide the map section")
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
    conference = models.ForeignKey(Conference, on_delete=models.CASCADE, related_name='organizers')
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='organizers/', blank=True, null=True)
    order = models.PositiveIntegerField(default=0, help_text="Display order")
    
    def __str__(self):
        return f"{self.name} - {self.conference.title}"
    
    class Meta:
        ordering = ['order', 'name']

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

class ImportantDate(models.Model):
    conference = models.ForeignKey(Conference, on_delete=models.CASCADE, related_name='important_dates')
    title = models.CharField(max_length=200, help_text="e.g., 'Paper Submission Deadline', 'Registration'")
    date = models.DateField(null=True, blank=True, help_text="Leave empty if using status text only")
    status_text = models.CharField(max_length=100, blank=True, help_text="e.g., 'CLOSED', 'OPEN' - shown instead of date if provided")
    is_closed = models.BooleanField(default=False, help_text="Show as 'CLOSED' status")
    order = models.PositiveIntegerField(default=0, help_text="Display order")
    
    def __str__(self):
        if self.status_text:
            return f"{self.title}: {self.status_text}"
        elif self.date:
            return f"{self.title}: {self.date.strftime('%B %d, %Y')}"
        else:
            return self.title
    
    def get_display_text(self):
        """Returns the text to display for this date"""
        if self.is_closed:
            return "CLOSED"
        elif self.status_text:
            return self.status_text
        elif self.date:
            return self.date.strftime('%B %d, %Y')
        else:
            return ""
    
    class Meta:
        ordering = ['order', 'title']

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
    content = models.TextField(help_text="Agenda item content (supports markdown for lists, formatting, etc.)")
    icon = models.CharField(max_length=20, choices=ICON_CHOICES, default='keynote')

    def __str__(self):
        # Show first 50 characters of content for display
        content_preview = self.content[:50] + "..." if len(self.content) > 50 else self.content
        return f"{self.time_start} - {content_preview}"

    class Meta:
        ordering = ['time_start']
