#from django.http import Http404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.shortcuts import render
from django.template import RequestContext
from django.utils import timezone

from notes.models import Note
# Create your views here.

def index(request):
    all_notes = Note.objects.all()
    return render(request, 'notes/index.html', {'all_notes': all_notes})

def detail(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    return render(request, 'notes/detail.html', {'note': note})

def urgent(request):
	urgent_notes = Note.objects.filter(urgent=True)
	context = {'urgent_notes': urgent_notes}
	return render(request, 'notes/urgent.html', context)

def unresolved(request):
	unresolved_notes = Note.objects.filter(resolved=False)
	context = {'unresolved_notes': unresolved_notes}
	return render(request, 'notes/unresolved.html', context)