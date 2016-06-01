from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages
from .models import Post
from .forms import PostForm
# Create your views here.

def post_create(request):
	form = PostForm(request.POST or None)
	if form.is_valid():
		new_post = form.save(commit=False)
		new_post.save()
		messages.success(request, "Successfully created.")
		return HttpResponseRedirect(new_post.get_absolute_url())

	return render(request, "posts/post_form.html",{"form":form})



def post_detail(request, id):
	post = get_object_or_404(Post, id=id)
	return render(request, "posts/post_detail.html", {"post":post})



def post_list(request):
	posts = Post.objects.all()
	return render(request, "posts/index.html", {"posts":posts})



def post_update(request, id):
	post = get_object_or_404(Post, id=id)
	form = PostForm(request.POST or None, instance=post)
	if form.is_valid():
		new_post = form.save(commit=False)
		new_post.save()
		messages.success(request, "Edit saved.")
		return HttpResponseRedirect(post.get_absolute_url())
	
	return render(request, "posts/post_update.html", {"post":post, "form":form})



def post_delete(request, id=None):
	post = get_object_or_404(Post, id=id)
	post.delete()
	messages.success(request, "Post deleted")
	return redirect("posts:list")