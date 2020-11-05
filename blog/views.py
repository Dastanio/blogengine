from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Tag
from django.views.generic import View
from .utils import *
from .forms import TagForm, PostForm
from django.urls import reverse

def post_lists(request):
    posts = Post.objects.order_by('-date_pub')
    return render(request,'blog/index.html', context = {'posts':posts})

class PostCreate(ObjectCreateMixin,View):
	form_model = PostForm
	template = 'blog/post_create.html'

	
class PostDetail(ObjectDetailMixin, View):
	model = Post
	template = 'blog/post_detail.html'


class TagDetail(ObjectDetailMixin, View):
	model = Tag
	template = 'blog/tag_detail.html'


class TagCreate(ObjectCreateMixin,View):
	form_model = TagForm
	template = 'blog/tag_create.html'

class TagUpdate(ObjectUpdateMixin, View):
	model = Tag
	form_model = TagForm
	template = 'blog/tag_update_form.html'

class PostUpdate(ObjectUpdateMixin, View):
	model = Post
	form_model = PostForm
	template = 'blog/post_update_form.html'

class TagDelete(View):
	def get(self, request, slug):
		tag = Tag.objects.get(slug__iexact = slug)
		return render(request, 'blog/tag_delete_form.html', context = {'tag':tag})
	def post(self, request, slug):
		tag = Tag.objects.get(slug__iexact = slug)
		tag.delete()
		return redirect(reverse('tags_list_url'))


def tags_list(request):
	tags = Tag.objects.all()
	return render(request, 'blog/tags_list.html', context={'tags':tags})



'''
class TagUpdate(View):
	def get(self, request, slug):
		tag = Tag.objects.get(slug__iexact = slug)
		bound_form = TagForm(instance  = tag)
		return render(request, 'blog/tag_update_form.html', context = {'form': bound_form, 'tag': tag})

	def post(self, request, slug):
		tag = Tag.objects.get(slug__iexact = slug)
		bound_form = TagForm(request.POST, instance  = tag)
		if bound_form.is_valid():
			update_tag = bound_form.save()
			return redirect(update_tag)
		return request(request, 'blog/tag_update_form.html', {'form': bound_form, 'tag': tag})'''
		