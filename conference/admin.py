from django.contrib import admin
from .models import Conference, Person, ImportantDate, Speaker, AgendaItem

class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'affiliation')
    search_fields = ('name', 'title', 'affiliation')

class ImportantDateInline(admin.TabularInline):
    model = ImportantDate
    extra = 1

class SpeakerInline(admin.TabularInline):
    model = Speaker
    extra = 1

class AgendaItemInline(admin.TabularInline):
    model = AgendaItem
    extra = 1

class ConferenceAdmin(admin.ModelAdmin):
    list_display = ('title', 'year', 'date', 'location')
    list_filter = ('year',)
    search_fields = ('title', 'description', 'location')
    inlines = [ImportantDateInline, SpeakerInline, AgendaItemInline]
    filter_horizontal = ('general_chairs', 'program_chairs', 'organizers')

admin.site.register(Conference, ConferenceAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(ImportantDate)
admin.site.register(Speaker)
admin.site.register(AgendaItem)
