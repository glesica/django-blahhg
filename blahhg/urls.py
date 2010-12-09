from django.conf.urls.defaults import *

urlpatterns = patterns('django.views.generic.simple',
    (r'^$',               'direct_to_template', {'template': 'blahhg/entry_list.html'}),
    (r'^(?P<slug>[a-z0-9-]+)/$', 'direct_to_template', {'template': 'blahhg/entry_detail.html'}),
)
