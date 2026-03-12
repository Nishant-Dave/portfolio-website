from django import template
import markdown as md
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter(name='markdown_format')
def markdown_format(text):
    """
    Converts markdown text to HTML, enabling syntax highlighting
    for fenced code blocks.
    """
    if not text:
        return ""
    
    html = md.markdown(
        text,
        extensions=[
            'markdown.extensions.fenced_code', # Allows ```python code blocks
            'markdown.extensions.codehilite',  # Enables Pygments highlighting
            'markdown.extensions.tables',      # Support for markdown tables
        ]
    )
    return mark_safe(html)
