from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class AllNotesManager(models.Manager):
    def get_queryset(self):
        return super(AllNotesManager, self).get_queryset().all().order_by('-created')

class UnresolvedNoteManager(models.Manager):
    def get_queryset(self):
        return super(UnresolvedNoteManager, self).get_queryset().filter(resolved=False)

class UrgentNoteManager(models.Manager):
    def get_queryset(self):
        return super(UrgentNoteManager, self).get_queryset().filter(urgent=True, resolved=False)


class Note(models.Model):
	subject = models.CharField(max_length = 200)
	description = models.TextField(blank=True)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	urgent = models.BooleanField()
	resolved = models.BooleanField()

	all_notes = AllNotesManager()
	unresolved_notes = UnresolvedNoteManager()
	urgent_notes = UrgentNoteManager()

	def __unicode__(self):
		return self.subject


class Update(models.Model):
	subject = models.CharField(max_length = 200)
	description = models.TextField(blank=True)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	note = models.ForeignKey(Note)

	def __unicode__(self):
		return u'%s %s' % (self.subject, self.note)
