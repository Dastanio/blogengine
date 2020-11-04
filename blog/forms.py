from django.forms import ModelForm, TextInput, Textarea, SelectMultiple
from .models import Tag, Post
from django.core.exceptions import ValidationError

class TagForm(ModelForm):
	class Meta:
		model = Tag
		fields = ['title', 'slug']

		widgets = {
			'title': TextInput(attrs = {'class': 'form-control'}),
			'slug': TextInput(attrs = {'class': 'form-control'}),
		}

	def clean_slug(self):
		new_slug = self.cleaned_data['slug'].lower()

		if new_slug == 'create':
			raise ValidationError('Slug may not "create" ')
			return new_slug
		return new_slug

class PostForm(ModelForm):
	class Meta:
		model = Post
		fields = ['title', 'slug', 'body', 'tags']

		widgets = {
			'title': TextInput(attrs= {'class': 'form-control'}),
			'slug': TextInput(attrs= {'class': 'form-control'}),
			'body': Textarea(attrs= {'class': 'form-control'}),
			'tags': SelectMultiple(attrs= {'class': 'form-control'}),
		}

	def clean_slug(self):
		new_slug = self.cleaned_data['slug'].lower()

		if new_slug == 'create':
			raise ValidationError('slug may not a "create" ')
		return new_slug

