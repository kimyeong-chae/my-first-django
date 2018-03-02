# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import *
from django.utils import timezone
from .models import Post
from .forms import PostForm
import logging

def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/post_detail.html', {'post':post})

def post_new(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('post_list')
	else:
		form = PostForm()
	return render(request, 'blog/post_edit.html', {'form':form})

def post_edit(request, pk):
	logger = logging.getLogger()
	logger.info('post_edit')
	post = get_object_or_404(Post, pk=pk)
	if request.method == "POST":
		logger.info('포스트다')
		form = PostForm(instance=post)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			logger.info('여기다여기')
			return redirect('post_detail', pk=post.pk)
	else:
		logger.info('포스트가 아니다')
		form = PostForm(instance=post)
	return render(request, 'blog/post_edit.html', {'form':form})
