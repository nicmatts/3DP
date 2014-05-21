from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Note(models.Model):
	subject = models.CharField(max_length = 200)
	description = models.TextField(blank=True)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	urgent = models.BooleanField()
	resolved = models.BooleanField()

	def __unicode__(self):
		return self.subject