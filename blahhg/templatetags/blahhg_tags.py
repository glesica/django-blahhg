from django import template
from django.conf import settings

from ..models import BlahhgEntry

register = template.Library()

@register.inclusion_tag('blahhg/entry-detail.html')
def blahhg_entry_detail(entry_slug=None):
    """
    Inserts the entry corresponding to `entry_slug` into the template.
    If `entry_slug` is not given, inserts the newest live entry.
    """
    # Default to latest entry unless we got a slug, then load the correct 
    # entry. If entry doesn't exist just stick with latest to avoid errors.
    entry = BlahhgEntry.live.latest()
    if entry_slug:
        try:
            entry = BlahhgEntry.live.filter(slug=entry_slug)
        except BlahhgEntry.DoesNotExist:
            pass
    
    return {'entry': entry}

@register.inclusion_tag('blahhg/entry-list.html')
def blahhg_entry_list(num=None):
    """
    Inserts a list of entries into the template. If `num` is provided 
    then no more than that number of entries will be returned.
    """
    number_of_entries = settings.BLAHHG_LIST_SIZE
    if num is not None:
        try:
            number_of_entries = int(num)
        except (ValueError, TypeError):
            pass
        
    entries = BlahhgEntry.live.all()[:number_of_entries]
    
    return {'entries': entries}

