#from django.http import Http404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render_to_response, redirect, render
from django.template import RequestContext
from django.utils import timezone

import re

from notes.models import Note
from notes.models import Update
from notes.forms import NoteForm
from notes.forms import	UpdateForm
#from updates.models import Update
# Create your views here.

@login_required
def all_notes(request):
    all_notes = Note.all_notes.all()
    unresolved_notes = Note.unresolved_notes.all()
    urgent_notes = Note.urgent_notes.all()
    return render_to_response('notes/index.html', {'all_notes': all_notes, 'unresolved_notes': unresolved_notes, 'urgent_notes': urgent_notes}, context_instance=RequestContext(request))

# def index(request):
# 	if (re.match("/notes/urgent/", request.path)):
# 		notes = Note.objects.filter(urgent=True)
# 		return render_to_response('notes/index.html', {'notes': notes, 'messageheader' : 'Urgent Messages'}, context_instance=RequestContext(request))
# 	elif (re.match("/notes/unresolved/", request.path)):
# 		notes = Note.objects.filter(resolved=False)
# 		return render_to_response('notes/index.html', {'notes': notes, 'messageheader' : 'Unresolved Messages'}, context_instance=RequestContext(request))		
# 	else:
# 		notes = Note.objects.all()
# 		return render_to_response('notes/index.html', {'notes': notes, 'messageheader' : 'Message Center'}, context_instance=RequestContext(request))

@login_required
def add_note(request):
	if request.method == 'POST':
		form = NoteForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
	else:
		form = NoteForm()
	return render(request, 'notes/add_note.html', {'form': form})

@login_required
def note_detail(request, note_id):
    item = get_object_or_404(Note, pk=note_id)
    update = Update.objects.filter(note=note_id)
    print update
    return render(request, 'notes/detail.html', {'item': item, 'update': update})

# def note_urgent(request):
# 	urgent_notes = Note.urgent_notes.all()
# 	context = {'urgent_notes': urgent_notes}
# 	return render(request, 'notes/urgent.html', context)

# def note_unresolved(request):
# 	unresolved_notes = Note.unresolved_notes.all()
# 	context = {'unresolved_notes': unresolved_notes}
# 	return render(request, 'notes/unresolved.html', context)

def note_edit(request, note_id):
	note = get_object_or_404(Note, pk=note_id)
	if request.method=='POST':
		form = NoteForm(request.POST, instance=note)
		if form.is_valid():
			form.save()
			return redirect('note_detail', note_id)
	else:
		form = NoteForm(instance=note)
	return render_to_response('notes/note_edit.html', {'form': form}, context_instance=RequestContext(request))

def add_update(request, note_id):
	note = Note.all_notes.get(pk=note_id)
	form = UpdateForm(request.POST)
	if request.method == 'POST':
		if form.is_valid():
			update = form.save(commit=False)
			update.note = note
			update.save()
			return redirect('note_detail', note_id)
		else:
			form = UpdateForm()	
	else:
		form = UpdateForm()
	return render_to_response('notes/add_update.html', {'form': form},  context_instance=RequestContext(request))
