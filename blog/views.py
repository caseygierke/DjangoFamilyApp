from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .forms import PostForm
from .models import Post

# Create your views here.
def post_list(request):
	posts = Post.objects.order_by('name')
	stuff_for_frontend = {'posts': posts}
	return render(request, 'blog/post_list.html', stuff_for_frontend)

def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	stuff_for_frontend = {'post': post}
	return render(request, 'blog/post_detail.html', stuff_for_frontend)

def post_new(request):
	# If someone is doing a Post request, do this stuff
	if request.method == 'POST':
		form = PostForm(request.POST, request.FILES)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('post_detail', pk=post.pk)
	else:
		# See all the items in that dictionary object
		# print(request.__dict__)
		form = PostForm()
		stuff_for_frontend = {'form': form}
	return render(request, 'blog/post_edit.html', stuff_for_frontend)

def post_edit(request, pk):
	post = get_object_or_404(Post, pk=pk)
	if request.method == 'POST':

		#Update an existing form
		form = PostForm(request.POST, instance=post)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('post_detail',pk=post.pk)
	else:
		# If I am just showing up and it is using the GET method
		# then just show me the existing post 
		form = PostForm(instance=post)
		stuff_for_frontend = {'form': form}
	return render(request, 'blog/post_edit.html', stuff_for_frontend)
