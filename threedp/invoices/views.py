#from django.http import Http404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render_to_response, redirect, render
from django.template import RequestContext
from django.utils import timezone

from invoices.models import Invoice
from invoices.forms import InvoiceForm

@login_required
def index(request):
    all_jobs = Invoice.all_invoices.all()
    queued_jobs = Invoice.queued_invoices.all()
    queued_jobs_count = queued_jobs.count()
    running_jobs = Invoice.running_invoices.all()
    running_jobs_count = running_jobs.count()
    return render_to_response('invoices/index.html', {'all_jobs': all_jobs, 'queued_jobs': queued_jobs, 'running_jobs': running_jobs, 'queued_jobs_count': queued_jobs_count, 'running_jobs_count': running_jobs_count}, context_instance=RequestContext(request))


@login_required
def add_job(request):
	if request.method == 'POST':
		form = InvoiceForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
	else:
		form = InvoiceForm()
	return render(request, 'invoices/add_job.html', {'form': form})

@login_required
def job_detail(request, invoice_id):
    job = get_object_or_404(Invoice, pk=invoice_id)
    return render_to_response('invoices/job_detail.html', {'job': job}, context_instance=RequestContext(request))

@login_required
def job_edit(request, invoice_id):
	invoice = get_object_or_404(Invoice, pk=invoice_id)
	if request.method=='POST':
		form = InvoiceForm(request.POST, instance=invoice)
		if form.is_valid():
			form.save()
			return redirect('job_detail', invoice_id)
	else:
		form = InvoiceForm(instance=invoice)
	return render_to_response('invoices/job_edit.html', {'form': form}, context_instance=RequestContext(request))