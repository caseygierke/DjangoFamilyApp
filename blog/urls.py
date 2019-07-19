from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
# from django.contrib.auth import views as auth_views

urlpatterns = [
	path('', views.post_list, name='post_list'),
	path('post/<int:pk>/', views.post_detail, name='post_detail'),
	path('post/new/', views.post_new, name='post_new'),
	path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
	path('drafts/', views.post_draft_list, name='post_draft_list'),	
	path('post/<int:pk>/publish/', views.post_publish, name='post_publish'),
	path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
	path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),
	path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
	path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
	path('signup/', views.signup, name='signup'),
	# path('accounts/', include(django.contrib.auth.urls)),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
	