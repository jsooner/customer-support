from django.db import models

# Create your models here.
class Response(models.Model):
	title  = models.CharField(max_length=100, blank=True)
	body = models.TextField(blank=True)
	to_email = models.EmailField()

	def __str__(self):
		return f'{self.id} Subject Title: {self.title}, Active: {self.active}'