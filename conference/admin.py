from django.contrib import admin
from .models import Conference, Speaker, AgendaItem, Organizer

class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'affiliation')
    search_fields = ('name', 'title', 'affiliation')



class SpeakerInline(admin.TabularInline):
    model = Speaker
    extra = 1

class AgendaItemInline(admin.TabularInline):
    model = AgendaItem
    extra = 1

class OrganizerInline(admin.TabularInline):
    model = Organizer
    extra = 1

class ConferenceAdmin(admin.ModelAdmin):
    list_display = ('title', 'year', 'date', 'location')
    list_filter = ('year',)
    search_fields = ('title', 'description', 'location')

admin.site.register(Conference, ConferenceAdmin)
admin.site.register(Speaker)
admin.site.register(AgendaItem)
admin.site.register(Organizer)
