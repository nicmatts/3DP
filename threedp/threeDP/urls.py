from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', 'threeDP.views.index', name='home'),
    url(r'^messages/', include('notes.urls')),
    url(r'^jobs/', include('invoices.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^comments/', include('django_comments.urls')),
    url(r'^login/$', 'threeDP.views.login_page', name='login'),
    url(r'^logout/$', 'threeDP.views.logout_view', name='logout'),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)