from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext
from django.shortcuts import render_to_response, render, redirect

from .forms import LoginForm
from notes.models import Note
from invoices.models import Invoice
from invoices.forms import InvoiceForm

def login_page(request):
	message = None
	if request.method ==  "POST":
		form = LoginForm(request.POST)
		if form.is_valid():
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(username=username, password=password)
			if user is not None:
				if user.is_active:
					login(request, user)
					return redirect('home')
				else:
					message = "Invalid username and/or password."
	else:
		form = LoginForm()
	return render_to_response('login.html', {'message': message, 'form': form}, context_instance=RequestContext(request))

def logout_view(request):
    logout(request)
    return render_to_response('index.html', context_instance=RequestContext(request))

def add_job(request):
	if request.method == 'POST':
		form = InvoiceForm(request.POST)
		if form.is_valid():
			form.save()
			return form
	else:
		form = InvoiceForm()
	return render(request, 'invoices/add_job.html', {'form': form})

def index(request):
	all_notes = Note.all_notes.all()
	unresolved_notes = Note.unresolved_notes.all()
	urgent_notes = Note.urgent_notes.all()
	queued_invoices = Invoice.queued_invoices.all()
	running_invoices = Invoice.running_invoices.all()
	form = InvoiceForm(request.POST)
	if form.is_valid():
		form.save()
		return form
	#return render(request, 'invoices/add_job.html', {'form': form})
	return render_to_response('index.html', {'all_notes': all_notes, 'unresolved_notes': unresolved_notes, 'urgent_notes': urgent_notes, 'queued_invoices': queued_invoices, 'running_invoices': running_invoices, 'form': form}, context_instance=RequestContext(request))
    

#@login_required
def start_job(request):
	if request.method == 'POST':
		form = InvoiceForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
	else:
		form = InvoiceForm()
	return render(request, 'index.html', {'form': form})
