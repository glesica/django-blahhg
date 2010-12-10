from django.conf.urls.defaults import *
from django.conf import settings

from blahhg.models import BlahhgEntry

urlpatterns = patterns('django.views.generic',
    (r'^$', 'list_detail.object_list', {
        'queryset':             BlahhgEntry.live.all(),
        'template_name':        'blahhg/blog.html',
        'paginate_by':          settings.BLAHHG_LIST_SIZE,
        'template_object_name': 'entry',
    }),
    (r'^archive/(?P<slug>[a-z0-9-]+)/$', 'list_detail.object_detail', {
        'queryset':             BlahhgEntry.live.all(),
        'template_name':        'blahhg/entry.html',
        'template_object_name': 'entry',
    }),
)
