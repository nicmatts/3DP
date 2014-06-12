from django.conf.urls import patterns, url

from notes import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<note_id>\d+)/$', views.note_detail, name='note_detail'),
    url(r'^(?P<note_id>\d+)/edit/$', views.note_edit, name='note_edit'),
    url(r'^add/$', views.add_note, name='add_note'),
    url(r'^(?P<note_id>\d+)/update/$', views.add_update, name='add_update'),
    #url(r'^urgent/$', views.note_urgent, name='note_urgent'),
    #url(r'^unresolved/$', views.note_unresolved, name='note_unresolved'),
)