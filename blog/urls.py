"""Copyright Johnathan Crocker 2017"""
from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.post_list, name='post_list'),
	url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
	url(r'^post/new/$', views.post_new, name='post_new'),
	url(r'^post/edit/(?P<pk>\d+)/$', views.post_edit, name='post_edit'),
	url(r'^post/remove/(?P<pk>\d+)/$', views.post_remove, name='post_remove'),
	url(r'^drafts/$', views.post_draftList, name='post_draftList'),
	url(r'^post/publish/(?P<pk>\d+)/$', views.post_publish, name='post_publish'),
	url(r'^post/unpublish/(?P<pk>\d+)/$', views.post_unpublish, name='post_unpublish'),
	url(r'^accounts/new/$', views.account_new, name='account_new'),
	url(r'^post/(?P<pk>\d+)/comment/$', views.comment_post, name='comment_post'),
]