from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.

class Permission(models.Model):
	user = models.ForeignKey('auth.User')
	can_post = models.BooleanField(default=False)
	
	@property
	def name(self):
		return self.user.username
	
	def __str__(self):
		return self.user.username;

class Post(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=256)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)
	
	def publish(self):
		self.published_date = timezone.now()
		self.save()
		
	def unpublish(self):
		self.published_date = None
		self.save()
		
	def __str__(self):
		return self.title
	