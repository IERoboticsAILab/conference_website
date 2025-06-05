from django.shortcuts import render, get_object_or_404, redirect
from .models import Conference, AgendaItem, Speaker

def home(request):
    """Redirect to the latest conference year"""
    try:
        latest_conference = Conference.objects.latest('year')
        return redirect('conference_year', year=latest_conference.year)
    except Conference.DoesNotExist:
        # If no conferences exist, show an empty page or create a default one
        return render(request, 'conference/no_conferences.html')

def conference_year(request, year):
    """Single comprehensive page for each conference year"""
    conference = get_object_or_404(Conference, year=year)
    
    # Get all related data for the conference
    agenda_items = conference.agenda_items.all()
    speakers = conference.speakers.all()
    
    # Get all available years for navigation
    all_years = Conference.objects.values_list('year', flat=True).order_by('-year')
    
    return render(request, 'conference/year_page.html', {
        'conference': conference,
        'agenda_items': agenda_items,
        'speakers': speakers,
        'all_years': all_years,
        'current_year': year,
    })

def livestream(request):
    """Simple livestream page"""
    return render(request, 'conference/livestream.html')
