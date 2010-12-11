from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Atom1Feed
from django.core.urlresolvers import reverse
from django.conf import settings

from blahhg.models import BlahhgEntry

class RssFeed(Feed):
    title = settings.BLAHHG_TITLE
    link = '/blog/' #TODO fix this crap
    description = settings.BLAHHG_DESCRIPTION
    
    def items(self):
        return BlahhgEntry.live.all()[:settings.BLAHHG_FEED_SIZE]

class AtomFeed(RssFeed):
    feed_type = Atom1Feed
    subtitle = RssFeed.description
