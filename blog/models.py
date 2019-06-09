from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	name = models.CharField(max_length=200, unique=True)
	date_of_birth = models.DateTimeField(blank=True, null=True)
	date_deceased = models.DateTimeField(blank=True, null=True)
	parents = models.CharField(max_length=100, blank=True, null=True)
	spouse = models.CharField(max_length=100, blank=True, null=True)
	children =  models.CharField(max_length=300, blank=True, null=True)
	city =  models.CharField(max_length=100, blank=True, null=True)
	text = models.TextField()
	picture = models.ImageField(blank=True, upload_to='images/', default='images/IMG_3232.JPG')
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.name