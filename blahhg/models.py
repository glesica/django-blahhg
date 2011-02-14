from datetime import datetime
import markdown

from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from taggit.managers import TaggableManager

from blahhg.managers import LiveEntryManager


class BlahhgEntry(models.Model):
    """
    A blog entry.
    """
    LIVE_STATUS = 1
    DRAFT_STATUS = 2
    HIDDEN_STATUS = 3
    STATUS_CHOICES = (
        (LIVE_STATUS, 'Live'),
        (DRAFT_STATUS, 'Draft'),
        (HIDDEN_STATUS, 'Hidden'),
    )
    
    # Metadata.
    author = models.ForeignKey(User)
    enable_comments = models.BooleanField(
        default=True,
    )
    pub_date = models.DateTimeField(
        u'Date posted',
        default=datetime.today
    )
    status = models.IntegerField(
        choices=STATUS_CHOICES,
        default=LIVE_STATUS,
        help_text=u'Only entries with "live" status will be displayed publicly.'
    )
    title = models.CharField(
        max_length=140,
    )
    slug = models.SlugField(
        unique=True,
        help_text='Used in the URL of the entry. Must be unique.'
    )
    
    # The actual entry bits.
    body = models.TextField()
    body_html = models.TextField(
        editable=False,
        blank=True,
    )
    excerpt = models.TextField(
        blank=True,
        null=True,
    )
    excerpt_html = models.TextField(
        editable=False,
        blank=True,
        null=True,
    )
    auto_excerpt = models.BooleanField(
        default=False,
        help_text='If set an excerpt will always be auto-generated, overwriting any custom excerpt.',
    )
    
    # Tagging.
    tags = TaggableManager()
    
    # Managers
    live = LiveEntryManager()
    objects = models.Manager()
    
    class Meta:
        get_latest_by = 'pub_date'
        ordering = ['-pub_date']
        verbose_name = 'Entry'
        verbose_name_plural = 'Entries'
    
    class Admin:
        date_hierarchy = 'pub_date'
        fields = (
            ('Metadata', { 'fields':
                ('title', 'slug', 'pub_date', 'author', 'status', 'enable_comments') }),
            ('Entry', { 'fields':
                ('excerpt', 'auto_excerpt', 'body') }),
            ('Tags', { 'fields':
                ('tags',) }),
            )
        list_display = ('title', 'pub_date', 'author', 'status', 'enable_comments')
        list_filter = ('status',)
    
    def __unicode__(self):
        return self.title
    
    def save(self):
        if not self.excerpt or self.auto_excerpt:
            # split up on double line breaks (paragraphs) and take paragraphs
            # from the beginning such that total length < AUTO_EXCERPT_SIZE
            # always include at least one paragraph
            total = 0
            paragraphs = []
            for para in self.body.split('\r\n\r\n'): #TODO make sure this is consistent
                if total < 200: #TODO add this to settings
                    total += len(para)
                    paragraphs.append(para)
            self.excerpt = '\n\n'.join(paragraphs)
            
        # Add the "Read More" link.
        #TODO Needs to be customizable
        #TODO Should be translated
        self.excerpt += ' <a href="%s" title="%s">Read More</a>' % (self.get_absolute_url(), self.title)
        
        self.excerpt_html = markdown.markdown(self.excerpt)
        self.body_html = markdown.markdown(self.body)
        super(BlahhgEntry, self).save()
    
    def get_absolute_url(self):
        return reverse('blahhg-detail', kwargs={'slug': self.slug})
    
    def _next_previous_helper(self, direction):
        return getattr(self, 'get_%s_by_pub_date' % direction)(status__exact=self.LIVE_STATUS)
    
    def get_next(self):
        """
        Returns the next Entry with "live" status by ``pub_date``, if
        there is one, or ``None`` if there isn't.
        
        In public-facing templates, use this method instead of
        ``get_next_by_pub_date``, because ``get_next_by_pub_date``
        does not differentiate entry status.
        
        """
        return self._next_previous_helper('next')
    
    def get_previous(self):
        """
        Returns the previous Entry with "live" status by ``pub_date``,
        if there is one, or ``None`` if there isn't.
        
        In public-facing templates, use this method instead of
        ``get_previous_by_pub_date``, because
        ``get_previous_by_pub_date`` does not differentiate entry
        status..
        
        """
        return self._next_previous_helper('previous')


    
