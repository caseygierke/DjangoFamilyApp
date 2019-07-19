from django import forms
from .models import Post, Comment
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

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

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())
	helper = FormHelper()
	helper.form_method = 'POST'
	helper.add_input(Submit('Sign up', 'Sign up', css_class='btn-primary'))
	class Meta:
		model = User
		fields = ('username', 'email', 'password',)
