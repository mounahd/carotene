from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'person.views.index', name='index'),
    url(r'^participant$', 'person.views.create_participant', name='participants'),
    url(r'^admin/', include(admin.site.urls)),
)
