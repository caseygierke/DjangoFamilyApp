from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
	class Meta:
		# Select the model to generate
		model = Post
		# Pick which fields you want it to render, note 
		# that author will generate a drop down box because 
		# it uses the foreign key.  We will not use author
		fields = ('name', 'date_of_birth', 'date_deceased', 'parents', 'spouse', 'children', 'city', 'text', 'picture')

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('text',)