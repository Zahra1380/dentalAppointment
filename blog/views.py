from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import BlogModel, Visitors



class Blog(ListView):
    template_name = 'blog/blogs.html'
    paginate_by = 1
    context_object_name = 'blogs'
    model = BlogModel

class BlogDetail(DetailView):
    model = BlogModel
    template_name = 'blog/blog_detail.html'
    context_object_name = 'blog'

    def get_context_data(self, **kwargs):

        context = super(BlogDetail, self).get_context_data()
        obj = self.object

        if not Visitors.objects.filter(visitors=self.request.user, blog=obj):
            Visitors.objects.create(visitors=self.request.user, blog=obj)
        return context
