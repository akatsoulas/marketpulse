from django.conf import settings
from django.conf.urls import patterns, url

urlpatterns = patterns(
    '{0}.main.views'.format(settings.PROJECT_MODULE),
    url(r'^new/$', 'edit_fxosprice', name='new_fxosprice'),
    url(r'^(?P<username>[A-Za-z0-9_]+)/(?P<id>\d+)/$',
        'view_fxosprice', name='view_fxosprice'),
)
