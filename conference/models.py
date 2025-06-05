from django.db import models

class Conference(models.Model):
    year = models.PositiveIntegerField(unique=True)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
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
