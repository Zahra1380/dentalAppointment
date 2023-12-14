from django.urls import path, include
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.Blog.as_view (), name='blogs'),
    path('detail/<int:pk>', views.BlogDetail.as_view (), name='blog_detail'),
]
