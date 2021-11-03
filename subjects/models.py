from django.db import models

# Create your models here.
class Subjects(models.Model):
	title  = models.CharField(max_length=100, blank=True, null=True)
	slug  = models.SlugField(blank=True, null=True)
	body = models.TextField(blank=True, null=True)
	date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
	attatchment = models.FileField(upload_to='documents', blank=True, null=True)
	email = models.EmailField()
	#add in thumbnail later
	#add in author later
