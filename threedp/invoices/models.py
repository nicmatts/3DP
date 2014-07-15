from django.db import models
from django.http import HttpResponse

# Create your models here.

class AllInvoicesManager(models.Manager):
    def get_queryset(self):
        return super(AllInvoicesManager, self).get_queryset().all().order_by('-created')

class QueuedInvoicesManager(models.Manager):
    def get_queryset(self):
        return super(QueuedInvoicesManager, self).get_queryset().filter(job_state='queued')

class RunningInvoicesManager(models.Manager):
    def get_queryset(self):
        return super(RunningInvoicesManager, self).get_queryset().filter(job_state='running')

class CompletedInvoicesManager(models.Manager):
    def get_queryset(self):
        return super(CompletedInvoicesManager, self).get_queryset().filter(job_state='completed').order_by('-created')


class Invoice(models.Model):
	class Meta:
		verbose_name = "Job"
    	verbose_name_plural = "Jobs"

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
    	('AFIS', 'Accounting, Finance, and Information Systems'),
		('AES', 'Aerospace Studies'),
		('AAE', 'Agribusiness and Applied Economics'),
		('ABE', 'Agricultural and Biosystems Engineering'),
		('ALS', 'Allied Sciences'),
		('ANS', 'Animal Sciences'),
		('ADHM', 'Apparel, Design, and Hospitality Management'),
		('ALA', 'Architecture and Landscape Architecture'),
		('BIO', 'Biological Sciences'),
		('CBC', 'Chemistry and Biochemistry'),
		('CEE', 'Civil and Environmental Engineering'),
		('CPM', 'Coatings and Polymeric Materials'),
		('COM', 'Communication'),
		('CS', 'Computer Science'),
		('CME', 'Construction Management and Engineering'),
		('CJPS', 'Criminal Justice and Political Science'),
		('ED', 'Education'),
		('ECE', 'Electrical and Computer Engineering'),
		('EM', 'Emergency Management'),
		('ENG', 'English'),
		('FS', 'Food Systems'),
		('GEO', 'Geosciences'),
		('GS', 'Graduate School'),
		('HNES', 'Health, Nutrition, and Exercise Sciences'),
		('HPRS', 'History, Philosophy, and Religious Studies'),
		('HDFS', 'Human Development and Family Science'),
		('IME', 'Industrial and Manufacturing Engineering'),
		('IS', 'Interdisciplinary Studies'),
		('MM', 'Marketing and Management'),
		('MATH', 'Mathematics'),
		('ME', 'Mechanical Engineering'),
		('MS', 'Military Science'),
		('ML', 'Modern Languages'),
		('NRS', 'Natural Resource Sciences'),
		('NRS', 'Nursing'),
		('PA', 'Performing Arts'),
		('PHS', 'Pharmaceutical Sciences'),
		('PHP', 'Pharmacy Practice'),
		('PHY', 'Physics'),
		('PLP', 'Plant Pathology'),
		('PLS', 'Plant Sciences'),
		('PSY', 'Psychology'),
		('SA', 'Sociology and Anthropology'),
		('STAT', 'Statistics'),
		('US', 'University Studies'),
		('VMS', 'Veterinary and Microbiological Sciences'),
		('VA', 'Visual Arts'),
		('Other', 'Other'),
		('NA', 'N/A')
    )

	# time information
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	#customer information
	customer_first_name = models.CharField(max_length=20)
	customer_last_name = models.CharField(max_length=20)
	customer_email = models.EmailField()
	customer_phone = models.CharField(max_length=20)
	customer_status = models.CharField(max_length=10, choices=STATUS)
	customer_filename = models.CharField(max_length=200, blank=True, null=True)
	customer_purpose = models.CharField(max_length=10, choices=PURPOSE)
	customer_department = models.CharField(max_length=5, choices=DEPARTMENT, null=True)

	#job information
	sd_card_number = models.CharField(max_length=6, blank=True, null=True)
	filename = models.CharField(max_length=200)
	estimated_time = models.TimeField(auto_now_add=False, auto_now=False, blank=True, null=True)
	estimated_cost = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
	actual_time = models.TimeField(auto_now_add=False, auto_now=False, blank=True, null=True)
	job_cost = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
	description = models.TextField(blank=True, null=True)
	job_state = models.CharField(max_length=10, choices=STATE)

	all_invoices = AllInvoicesManager()
	queued_invoices = QueuedInvoicesManager()
	running_invoices = RunningInvoicesManager()
	completed_invoices = CompletedInvoicesManager()

	def __unicode__(self):
		return u'%s %s' % (self.id, self.filename)

	#def send_email(self):
		#return self.job_cost
		#add method for sending email


	#def print_invoice(self):
		#print invoice