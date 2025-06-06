from django.contrib import admin
from django.db import models
from django.forms import Textarea
from .models import Conference, Speaker, AgendaItem, Organizer, ConferenceRole, ImportantDate

class MarkdownWidget(Textarea):
    """Custom widget for markdown fields with helpful attributes"""
    def __init__(self, attrs=None):
        default_attrs = {
            'class': 'markdown-input',
            'rows': 20,
            'cols': 80,
            'placeholder': 'Enter markdown content here...'
        }
        if attrs:
            default_attrs.update(attrs)
        super().__init__(default_attrs)

@admin.register(Conference)
class ConferenceAdmin(admin.ModelAdmin):
    list_display = ['title', 'year', 'date', 'location']
    list_filter = ['year', 'date']
    search_fields = ['title', 'location', 'venue']
    ordering = ['-year']
    
    # Use custom widget for description field
    formfield_overrides = {
        models.TextField: {'widget': MarkdownWidget},
    }
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('year', 'title', 'date', 'location', 'venue', 'address')
        }),
        ('Hero Section', {
            'fields': ('hero_title', 'hero_subtitle', 'show_livestream', 'livestream_label', 'livestream_video_url'),
            'description': 'Configure the main hero section at the top of the page. Hero title defaults to conference title if empty.'
        }),
        ('Content (Markdown Enabled)', {
            'fields': ('description', 'call_for_papers'),
            'description': 'You can use markdown syntax in these fields. Preview will be available on the frontend.'
        }),
        ('Submission Button', {
            'fields': ('submission_button_text', 'submission_button_link'),
            'description': 'Configure the submission button that appears under the call for papers.'
        }),
    )

@admin.register(ImportantDate)
class ImportantDateAdmin(admin.ModelAdmin):
    list_display = ['title', 'conference', 'get_display_text', 'order']
    list_filter = ['conference', 'is_closed']
    search_fields = ['title', 'status_text']
    ordering = ['conference', 'order', 'title']
    list_editable = ['order']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('conference', 'title', 'order')
        }),
        ('Date/Status', {
            'fields': ('date', 'status_text', 'is_closed'),
            'description': 'Either set a date, or use status text, or check "is_closed" for CLOSED status.'
        }),
    )
    
    def get_display_text(self, obj):
        return obj.get_display_text()
    get_display_text.short_description = 'Display Text'

@admin.register(Speaker)
class SpeakerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'title', 'conference']
    list_filter = ['conference']
    search_fields = ['first_name', 'last_name', 'title']

@admin.register(AgendaItem)
class AgendaItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'conference', 'time_start', 'time_end', 'icon']
    list_filter = ['conference', 'icon']
    search_fields = ['title']
    ordering = ['conference', 'time_start']

@admin.register(Organizer)
class OrganizerAdmin(admin.ModelAdmin):
    list_display = ['name', 'conference', 'order']
    list_filter = ['conference']
    search_fields = ['name']
    ordering = ['conference', 'order', 'name']
    list_editable = ['order']
    
    fieldsets = (
        ('Organization Information', {
            'fields': ('conference', 'name', 'image')
        }),
        ('Display Options', {
            'fields': ('order',),
            'description': 'Lower numbers appear first'
        }),
    )

@admin.register(ConferenceRole)
class ConferenceRoleAdmin(admin.ModelAdmin):
    list_display = ['title', 'first_name', 'last_name', 'role_type', 'conference', 'order']
    list_filter = ['role_type', 'conference']
    search_fields = ['first_name', 'last_name', 'title', 'affiliation']
    ordering = ['conference', 'role_type', 'order', 'last_name']
    list_editable = ['order']
    
    fieldsets = (
        ('Personal Information', {
            'fields': ('title', 'first_name', 'last_name', 'affiliation')
        }),
        ('Role Information', {
            'fields': ('conference', 'role_type', 'order')
        }),
    )
