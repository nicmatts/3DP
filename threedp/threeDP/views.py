from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext
from django.shortcuts import render_to_response, render

from .forms import LoginForm
from notes.models import Note

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
					message = "You logged in with success."
				else:
					message = "Invalid username and/or password."
	else:
		form = LoginForm()
	return render_to_response('login.html', {'message': message, 'form': form}, context_instance=RequestContext(request))

def logout_view(request):
    logout(request)
    return render_to_response('index.html', context_instance=RequestContext(request))

def index(request):
    all_notes = Note.all_notes.all()
    unresolved_notes = Note.unresolved_notes.all()
    urgent_notes = Note.urgent_notes.all()
    return render(request, 'index.html', {'all_notes': all_notes, 'unresolved_notes': unresolved_notes, 'urgent_notes': urgent_notes})


