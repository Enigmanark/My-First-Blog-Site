from django.contrib import admin
from .models import Post, Permission


class PostAdmin(admin.ModelAdmin):
	"""The list display is used to display attributes of the model class in the admin model list"""
	list_display = ('title', 'author', 'created_date', 'published_date')
	"""Filters based on dates mostly it seems"""
	list_filter = ['created_date', 'published_date',]
	search_fields = ['title', 'text',]

# Register your models here.
admin.site.register([Post, Permission])