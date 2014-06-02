from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', 'threeDP.views.index', name='index'),
    url(r'^notes/', include('notes.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^comments/', include('django_comments.urls')),
    url(r'^login/$', 'threeDP.views.login_page', name='login'),
    url(r'^logout/$', 'threeDP.views.logout_view'),
)