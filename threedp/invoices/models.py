from django.db import models

# Create your models here.
class Invoice(models.Model):
	STATUS = (
		('student', 'student'),
		('faculty', 'faculty'),
		('staff', 'staff'),
    )

	PURPOSE = (
    	('academic', 'academic'),
    	('personal', 'personal'),
    )

	STATE = (
    	('queued', 'queued'),
    	('running', 'running'),
    	('completed', 'completed')
    )

	DEPARTMENT = (
    	('ART', 'Art'),
    	('CHEM', 'Chemistry'),
    	('MECHENG', 'Mechanical Engineering'),
    	('ZOO', 'ZOOLOGY')
    )

	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	customer_first_name = models.CharField(max_length=20)
	customer_last_name = models.CharField(max_length=20)
	customer_email = models.EmailField()
	customer_phone = models.CharField(max_length=20)
	customer_status = models.CharField(max_length=10, choices=STATUS)
	customer_department = models.CharField(max_length=10, choices=DEPARTMENT)
	customer_filename = models.CharField(max_length=200, blank=True)
	customer_purpose = models.CharField(max_length=10, choices=PURPOSE)

	sd_card_number = models.CharField(max_length=6, blank=True)
	filename = models.CharField(max_length=200, blank=True)
	estimated_time = models.TimeField(auto_now_add=False, auto_now=False, blank=True)
	actual_time = models.TimeField(auto_now_add=False, auto_now=False, blank=True)
	job_cost = models.DecimalField(max_digits=6, decimal_places=2, blank=True)
	description = models.TextField(blank=True)
	job_state = models.CharField(max_length=10, choices=STATE)

	def __unicode__(self):
		return self.id, self.filename

	#def send_email(self):
		#return self.job_cost
		#add method for sending email


	#def print_invoice(self):
		#print invoice