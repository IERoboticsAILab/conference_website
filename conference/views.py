from django.shortcuts import render, get_object_or_404, redirect
from .models import Conference, AgendaItem, Speaker, Organizer

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
    organizers = Organizer.objects.all()
    important_dates = conference.important_dates.all()
    
    # Get conference roles grouped by type
    general_chairs = conference.roles.filter(role_type='general_chair')
    program_chairs = conference.roles.filter(role_type='program_chair')
    conference_organizers = conference.roles.filter(role_type='organizer')
    
    # Get all available years for navigation
    all_years = Conference.objects.values_list('year', flat=True).order_by('-year')
    
    return render(request, 'conference/year_page.html', {
        'conference': conference,
        'agenda_items': agenda_items,
        'speakers': speakers,
        'organizers': organizers,
        'important_dates': important_dates,
        'general_chairs': general_chairs,
        'program_chairs': program_chairs,
        'conference_organizers': conference_organizers,
        'all_years': all_years,
        'current_year': year,
    })

def livestream(request):
    """Simple livestream page"""
    return render(request, 'conference/livestream.html')

def markdown_demo(request):
    """Demonstrate markdown extras functionality"""
    
    # Sample markdown content demonstrating all features
    markdown_demo_content = """
# Markdown Extras Demo

This page demonstrates the comprehensive markdown support available in your Django application.

[TOC]

## Text Formatting

**Bold text** and *italic text* work as expected. You can also use ~~strikethrough~~ and ==highlight== text.

You can create ^superscript^ and ~subscript~ text using PyMdown extensions.

## Code Highlighting

Inline code: `print("Hello, World!")`

### Python Code Block

```python
def fibonacci(n):
    '''Generate fibonacci sequence up to n'''
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()

# Call the function
fibonacci(1000)
```

### JavaScript Code Block

```javascript
// ES6 Arrow Function
const greet = (name) => {
    return `Hello, ${name}!`;
};

console.log(greet('World'));
```

## Tables

| Feature | Status | Description |
|---------|--------|-------------|
| Tables | ✅ | Full table support with alignment |
| Code Highlighting | ✅ | Syntax highlighting for 100+ languages |
| Math | ✅ | LaTeX-style math equations |
| Diagrams | ✅ | Mermaid diagram support |

## Task Lists

- [x] Set up markdown extras
- [x] Add syntax highlighting
- [x] Configure PyMdown extensions
- [ ] Add custom CSS themes
- [ ] Integrate with admin interface

## Math Equations

Inline math: $E = mc^2$

Block math:

$$
\\frac{n!}{k!(n-k)!} = \\binom{n}{k}
$$

## Admonitions

!!! note "Important Note"
    This is a note admonition. It's great for highlighting important information.

!!! warning "Be Careful"
    This is a warning admonition. Use it to draw attention to potential issues.

!!! tip "Pro Tip"
    This is a tip admonition. Perfect for sharing helpful advice.

## Keyboard Keys

To save a file, press ++ctrl+s++ on Windows/Linux or ++cmd+s++ on Mac.

Common shortcuts:
- Copy: ++ctrl+c++
- Paste: ++ctrl+v++
- Undo: ++ctrl+z++

## Emojis

You can use GitHub-style emojis: :smile: :rocket: :heart: :thumbsup:

## Footnotes

Here's a sentence with a footnote[^1].

Another sentence with a footnote[^note].

[^1]: This is the first footnote.
[^note]: This is a named footnote.

## Collapsible Details

??? success "Click to expand"
    This content is hidden by default and can be revealed by clicking the summary.

??? question "How does this work?"
    The details/summary HTML elements are used to create collapsible content.

## Mermaid Diagrams

```mermaid
graph TD
    A[Start] --> B{Is it working?}
    B -->|Yes| C[Great!]
    B -->|No| D[Debug]
    D --> B
    C --> E[End]
```

## Critic Markup

{--This text will be deleted--} {++This text will be added++}

{==This text will be highlighted==}

{>>This is a comment<<}

## Smart Symbols

Automatic conversion of common symbols:

- Copyright: (c) becomes ©
- Trademark: (tm) becomes ™
- Arrows: --> becomes →, <-- becomes ←
- Fractions: 1/2 becomes ½, 1/4 becomes ¼

## Block Quotes

> This is a blockquote.
> 
> It can span multiple lines and paragraphs.
> 
> > This is a nested blockquote.

## Definition Lists

Apple
:   A red or green fruit

Orange
:   A citrus fruit that's orange in color

Banana
:   A yellow curved fruit

## Abbreviations

*[HTML]: Hyper Text Markup Language
*[CSS]: Cascading Style Sheets
*[JS]: JavaScript

The HTML specification defines how CSS and JS work together.

---

This demonstrates the full power of markdown extras in your Django application! 🚀
"""
    
    return render(request, 'conference/markdown_demo.html', {
        'markdown_demo_content': markdown_demo_content,
    })
