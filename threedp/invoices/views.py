#from django.http import Http404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render_to_response, redirect, render
from django.template import RequestContext
from django.utils import timezone

from invoices.models import Invoice
from invoices.forms import NoteForm

@login_required
def index(request):
    all_jobs = Invoice.objects.all()
    return render(request, 'invoices/index.html', {'all_jobs': all_jobs})