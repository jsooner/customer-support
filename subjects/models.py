from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Subjects(models.Model):
	title  = models.CharField(max_length=100, blank=True)
	slug  = models.SlugField(blank=True)
	body = models.TextField(blank=True)
	date = models.DateTimeField(auto_now_add=True, blank=True)
	attatchment = models.FileField(upload_to='documents', blank=True)
	email = models.EmailField()
	rating = models.IntegerField(null=True,  default = None, validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ])
	active = models.BooleanField(default=True, null=True)

	def __str__(self):
		return f'{self.id} Subject Title: {self.title}, Active: {self.active}'
	#add in thumbnail later
	#add in author later
