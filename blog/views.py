"""Copyright Johnathan Crocker 2017"""
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Post, BlogUser, Comment
from .forms import PostForm, RegistrationForm, CommentForm

# Create your views here.
def account_new(request):
		if request.method == "POST":
			reg = RegistrationForm(request.POST)
			if reg.is_valid():
				password = reg.get_password() #get the password
				if password: #if the passwords matched, this will be the password, if not, this will be false
					BlogUser.objects.create_user(reg.get_username(), reg.get_email(), password)
					return redirect('login')
				else:
					reg = RegistrationForm()
					return render(request, 'blog/account_new.html', {'reg': reg, 'match': False})
		else:
			reg = RegistrationForm()
		return render(request, 'blog/account_new.html', {'reg': reg, 'match': True})
	
def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
	return render(request, 'blog/post_list.html', {'posts': posts})
		
	
def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	comments = Comment.objects.filter(post=post)
	form = CommentForm()
	return render(request, 'blog/post_detail.html', {'post': post, 'form': form, 'comments': comments,})

@login_required
def comment_post(request, pk):
	if request.method == "POST":
		form = CommentForm(request.POST)
		if form.is_valid():
			post = get_object_or_404(Post, pk=int(pk))
			comment = Comment(post=post, author=request.user, text=form.get_text())
			comment.save()
			return redirect('post_detail', pk=pk)
	else:
		return redirect('post_list')
	
@login_required	
def post_new(request):
	if not request.user.can_post:
		return redirect('post_list')
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.save()
			return redirect('post_detail', pk=post.pk)
	else:
		form = PostForm()
	
	return render(request, 'blog/post_edit.html', {'form': form})

@login_required	
def post_publish(request, pk):
	if not request.user.can_post:
		return redirect('post_list')
	post = get_object_or_404(Post, pk=pk)
	post.publish()
	return redirect('post_detail', pk=post.pk)

@login_required	
def post_unpublish(request, pk):
	if not request.user.can_post:
		return redirect('post_list')
	post = get_object_or_404(Post, pk=pk)
	post.unpublish()
	return redirect('post_detail', pk=post.pk)

@login_required		
def post_remove(request, pk):
	if not request.user.can_post:
		return redirect('post_list')
	post = get_object_or_404(Post, pk=pk)
	post.delete()
	return redirect('post_list')
	
@login_required	
def post_edit(request, pk):
	if not request.user.can_post:
		return redirect('post_list')
	post = get_object_or_404(Post, pk=pk)
	if request.method == "POST":
		form = PostForm(request.POST, instance=post)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.save()
			return redirect('post_detail', pk=post.pk)
	else:
		form = PostForm(instance=post)
	return render(request, 'blog/post_edit.html', {'form': form})
	
@login_required	
def post_draftList(request):
	if not request.user.can_post:
		return redirect('post_list')
	posts = Post.objects.filter(published_date__isnull=True).order_by('-created_date')
	return render(request, 'blog/post_draftList.html', {'posts': posts})
	