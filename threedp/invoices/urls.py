from django.conf.urls import patterns, url

from invoices import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^add/$', views.add_job, name='add_job'),
    url(r'^(?P<invoice_id>\d+)/$', views.job_detail, name='job_detail'),
    url(r'^(?P<invoice_id>\d+)/edit/$', views.job_edit, name='job_edit'),
)