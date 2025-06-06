import markdown
from django import template
from django.utils.safestring import mark_safe

register = template.Library()

# Configure markdown with comprehensive extensions
def get_markdown_instance():
    """Create a markdown instance with all useful extensions"""
    return markdown.Markdown(
        extensions=[
            # Core extensions
            'markdown.extensions.extra',  # Includes tables, fenced_code, footnotes, attr_list, def_list, abbr
            'markdown.extensions.codehilite',  # Syntax highlighting
            'markdown.extensions.toc',  # Table of contents
            'markdown.extensions.nl2br',  # Newline to break
            'markdown.extensions.sane_lists',  # Better list handling
            'markdown.extensions.smarty',  # Smart quotes and dashes
            'markdown.extensions.wikilinks',  # Wiki-style links
            'markdown.extensions.admonition',  # Call-out boxes
            
            # PyMdown extensions for enhanced features
            'pymdownx.arithmatex',  # Math support
            'pymdownx.betterem',  # Better emphasis handling
            'pymdownx.caret',  # Insert and superscript
            'pymdownx.critic',  # Critic markup
            'pymdownx.details',  # Collapsible details
            'pymdownx.highlight',  # Enhanced code highlighting
            'pymdownx.inlinehilite',  # Inline code highlighting
            'pymdownx.keys',  # Keyboard key styling
            'pymdownx.magiclink',  # Auto-link conversion
            'pymdownx.mark',  # Mark/highlight text
            'pymdownx.smartsymbols',  # Smart symbols
            'pymdownx.superfences',  # Enhanced fenced code blocks
            'pymdownx.tabbed',  # Tabbed content
            'pymdownx.tasklist',  # Task lists with checkboxes
            'pymdownx.tilde',  # Delete and subscript
        ],
        extension_configs={
            'markdown.extensions.codehilite': {
                'css_class': 'highlight',
                'use_pygments': True,
            },
            'pymdownx.highlight': {
                'css_class': 'highlight',
                'use_pygments': True,
                'linenums': True,
            },
            'pymdownx.superfences': {
                'custom_fences': [
                    {
                        'name': 'mermaid',
                        'class': 'mermaid',
                        'format': lambda source: f'<div class="mermaid">{source}</div>'
                    }
                ]
            },
                         'pymdownx.arithmatex': {
                 'generic': True,
             },
                          'markdown.extensions.toc': {
                 'permalink': False,
             },
        }
    )

@register.filter(name='markdown')
def markdown_filter(text):
    """
    Convert markdown text to HTML with extras.
    Usage: {{ content|markdown }}
    """
    if not text:
        return ''
    
    md = get_markdown_instance()
    html = md.convert(str(text))
    return mark_safe(html)

@register.filter(name='markdown_safe')
def markdown_safe_filter(text):
    """
    Convert markdown text to HTML with extras, but don't mark as safe.
    Usage: {{ content|markdown_safe }}
    """
    if not text:
        return ''
    
    md = get_markdown_instance()
    return md.convert(str(text))

@register.simple_tag
def markdown_css():
    """
    Include CSS for syntax highlighting and markdown styling.
    Usage: {% markdown_css %}
    """
    return mark_safe('''
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/styles/github.min.css">
    <style>
                 /* Minimal markdown content styling - headers inherit from conference.css */
         .markdown-content {
             line-height: 1.6;
         }
        
                 /* Basic typography - inherits from conference.css for headers */
         .markdown-content blockquote {
             border-left: 4px solid #ddd;
             margin: 1em 0;
             padding: 0 1em;
             color: #666;
         }
        
        .markdown-content table {
            border-collapse: collapse;
            width: 100%;
            margin: 1em 0;
        }
        
        .markdown-content th, .markdown-content td {
            border: 1px solid #ddd;
            padding: 8px 12px;
            text-align: left;
        }
        
        .markdown-content th {
            background-color: #f5f5f5;
            font-weight: 600;
        }
        
        .markdown-content code {
            background-color: #f5f5f5;
            padding: 2px 4px;
            border-radius: 3px;
            font-family: 'Courier New', monospace;
        }
        
        .markdown-content pre {
            background-color: #f8f8f8;
            border: 1px solid #ddd;
            border-radius: 4px;
            padding: 1em;
            overflow-x: auto;
            margin: 1em 0;
        }
        
        .markdown-content pre code {
            background: none;
            padding: 0;
        }
        
        /* Task list styling */
        .markdown-content .task-list-item {
            list-style-type: none;
        }
        
        .markdown-content .task-list-item input[type="checkbox"] {
            margin-right: 0.5em;
        }
        
        /* Admonition styling */
        .markdown-content .admonition {
            margin: 1em 0;
            padding: 1em;
            border-left: 4px solid #ccc;
            background-color: #f9f9f9;
        }
        
        .markdown-content .admonition.note { border-left-color: #3498db; }
        .markdown-content .admonition.warning { border-left-color: #f39c12; }
        .markdown-content .admonition.danger { border-left-color: #e74c3c; }
        .markdown-content .admonition.tip { border-left-color: #2ecc71; }
        
        .markdown-content .admonition-title {
            font-weight: 600;
            margin-bottom: 0.5em;
        }
        
        /* TOC styling */
        .markdown-content .toc {
            background-color: #f9f9f9;
            border: 1px solid #ddd;
            border-radius: 4px;
            padding: 1em;
            margin: 1em 0;
        }
        
        .markdown-content .toc ul {
            list-style-type: none;
            padding-left: 1em;
        }
        
        .markdown-content .toc > ul {
            padding-left: 0;
        }
        
        /* Highlight styling */
        .highlight {
            background-color: #f8f8f8;
            border: 1px solid #ddd;
            border-radius: 4px;
            padding: 1em;
            margin: 1em 0;
            overflow-x: auto;
        }
        
        /* Key styling */
        .keys kbd {
            background-color: #fafbfc;
            border: 1px solid #d1d5da;
            border-bottom-color: #c6cbd1;
            border-radius: 3px;
            box-shadow: inset 0 -1px 0 #c6cbd1;
            color: #444d56;
            display: inline-block;
            font-family: monospace;
            font-size: 11px;
            line-height: 10px;
            padding: 3px 5px;
            vertical-align: middle;
        }
        
        /* Mark/highlight text */
        .markdown-content mark {
            background-color: #fff3cd;
            padding: 2px 4px;
        }
    </style>
    ''')

@register.simple_tag
def markdown_js():
    """
    Include JavaScript for enhanced markdown features.
    Usage: {% markdown_js %}
    """
    return mark_safe('''
    <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
    <script>
        document.addEventListener('DOMContentLoaded', function() {
            // Initialize syntax highlighting
            hljs.highlightAll();
            
            // Initialize Mermaid diagrams
            mermaid.initialize({ startOnLoad: true });
            
            // Initialize MathJax if present
            if (window.MathJax) {
                MathJax.typesetPromise();
            }
        });
    </script>
    ''') 