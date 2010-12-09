from django.contrib import admin

from blahhg.models import BlahhgEntry

admin.site.register(BlahhgEntry, prepopulated_fields = {'slug':('title',),})


