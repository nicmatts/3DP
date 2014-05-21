from django.conf.urls import patterns, url

from notes import views

urlpatterns = patterns('',
    # ex: /notes/
    url(r'^$', views.index, name='index'),
    # ex: /notes/5/
    url(r'^(?P<note_id>\d+)/$', views.detail, name='detail'),

    url(r'^urgent/$', views.urgent, name='urgent'),
    #
    url(r'^unresolved/$', views.unresolved, name='unresolved'),
)