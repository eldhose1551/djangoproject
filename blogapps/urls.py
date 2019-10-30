from django.urls import path, include
from . import views
app_name = 'blogapps'

urlpatterns = [
    path('', views.blogs, name='blog'),
    path('create_blog/', views.create_blog, name='create_blog'),
    path('create_comment/', views.create_comment, name='create_comment'),
    path('article/<int:id>/', views.article, name='article'),
    path('delete_blog/<int:id>/', views.delete_blog, name='blog_delete'),
    path('update_blog/<int:id>/', views.update_blog, name='blog_update'),
    ]
