from .models import Footer

def footer_context(request):
    """Add footer data to all template contexts"""
    try:
        footer = Footer.objects.first()
        return {'footer': footer}
    except Footer.DoesNotExist:
        return {'footer': None} 