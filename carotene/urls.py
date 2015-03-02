from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'person.views.index', name='index'),
    url(r'^participant$', 'person.views.create_participant', name='participants'),
    url(r'^participants/(\d+)/$', 'person.views.view_participant', name='view_participant'),
    url(r'^mentor$', 'person.views.create_mentor', name='mentors'),
    url(r'^admin/', include(admin.site.urls)),
)
