from django.db import models


class LiveEntryManager(models.Manager):
    """
    Custom manager for the Entry model, providing shortcuts for
    filtering by entry status.
    """
    def get_query_set(self):
        """
        Overrides the default ``QuerySet`` to only include Entries
        with a status of 'live'.
        
        """
        return super(LiveEntryManager, self).get_query_set().filter(status__exact=self.model.LIVE_STATUS)

