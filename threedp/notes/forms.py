from django import forms

from notes.models import Note
from notes.models import Update

class NoteForm(forms.ModelForm):
	class Meta:
		model = Note

class UpdateForm(forms.ModelForm):
	class Meta:
		model = Update
		exclude = ('note',)