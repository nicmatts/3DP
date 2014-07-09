from django.shortcuts import render, redirect

from invoices.forms import InvoiceForm


def add_job(request):
	if request.method == 'POST':
		form = InvoiceForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
	else:
		form = InvoiceForm()
	return render(request, 'invoices/add_job.html', {'form': form})