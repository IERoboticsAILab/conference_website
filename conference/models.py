from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200, blank=True)
    affiliation = models.CharField(max_length=200, blank=True)
    bio = models.TextField(blank=True)
    image = models.ImageField(upload_to='people/', blank=True, null=True)

    def __str__(self):
        return self.name

class Conference(models.Model):
    year = models.PositiveIntegerField(unique=True)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    date = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=200)
    venue = models.CharField(max_length=200, blank=True)
    address = models.TextField(blank=True)
    general_chairs = models.ManyToManyField(Person, related_name='general_chairs', blank=True)
    program_chairs = models.ManyToManyField(Person, related_name='program_chairs', blank=True)
    organizers = models.ManyToManyField(Person, related_name='organizers', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} ({self.year})"

    class Meta:
        ordering = ['-year']

class ImportantDate(models.Model):
    conference = models.ForeignKey(Conference, on_delete=models.CASCADE, related_name='important_dates')
    title = models.CharField(max_length=200)
    date = models.DateField()
    is_deadline = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} - {self.date}"

    class Meta:
        ordering = ['date']

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
    conference = models.ForeignKey(Conference, on_delete=models.CASCADE, related_name='agenda_items')
    time = models.TimeField()
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    speakers = models.ManyToManyField(Speaker, blank=True)
    is_break = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.time} - {self.title}"

    class Meta:
        ordering = ['time']
