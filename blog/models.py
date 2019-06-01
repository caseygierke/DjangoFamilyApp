from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	name = models.CharField(max_length=200, unique=True)
	text = models.TextField()
	date_of_birth = models.DateTimeField(blank=True, null=True)
	date_deceased = models.DateTimeField(blank=True, null=True)
	published_date = models.DateTimeField(blank=True, null=True)
	picture = models.ImageField(blank=True, upload_to='images/', default='images/IMG_3232.JPG')

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.name