from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from subjects.models import Subjects

# Create your models here.
class Response(models.Model):
	title  = models.CharField(max_length=100, blank=True)
	body = models.TextField(blank=True)
	to_email = models.EmailField()
	subjectID = models.ForeignKey(Subjects, on_delete=CASCADE)
	staffID = models.ForeignKey(User, on_delete=CASCADE)

	def __str__(self):
		return f'{self.id} Response Title: {self.title}'