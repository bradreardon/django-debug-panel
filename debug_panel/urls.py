"""
URLpatterns for the debug panel.

These should not be loaded explicitly; It is used internally by the
debug-panel application.
"""
import django

_PREFIX = '__debug__'
_DEBUG_PANEL_URL = r'^%s/data/(?P<cache_key>\d+\.\d+)/$' % _PREFIX
_DJANGO_VERSION = float(django.get_version().rsplit('.', 1)[0])

if _DJANGO_VERSION > 1.4:
    from django.conf.urls import url
    from .views import debug_data

    urlpatterns = [
        url(_DEBUG_PANEL_URL, debug_data, name='debug_data'),
    ]
else:
    from django.conf.urls.defaults import patterns, url

    urlpatterns = patterns('debug_panel.views',
        url(_DEBUG_PANEL_URL, 'debug_data', name='debug_data'),
    )
