import datetime
from django.db import models
from django.utils import timezone
from django.conf import settings

AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')

# Create your models here.

class Shout(models.Model):
	shout_text = models.CharField(max_length=200)
	author_text = models.CharField(max_length=50)
	pub_date = models.DateTimeField('date published')
	# user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
	# maybe add logged in user to be a part of a shout?
	def __str__(self):
        	return self.shout_text + " " + self.author_text 