from django.views.generic import ListView, DetailView 
from django.views.generic.edit import UpdateView, DeleteView 
from django.urls import reverse_lazy 

from .models import Blog

class BlogListView(ListView):
    model=Blog
    template_name ='blog/blog_list.html'

class BlogDetailView(DetailView):
    model=Blog
    template_name ='blog/blog_detail.html'

class BlogUpdateView(UpdateView):
    model=Blog
    fields = ('title', 'body',)
    template_name ='blog/blog_edit.html'

class BlogDeleteView(DeleteView):
    model=Blog
    template_name ='blog/blog_delete.html'
    success_url = reverse_lazy('blog_list')