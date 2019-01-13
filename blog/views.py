from django.contrib.auth.mixins import LoginRequiredMixin 
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import UpdateView, DeleteView, CreateView 
from django.urls import reverse_lazy 

from .models import Blog

class BlogListView(ListView):
    model=Blog
    template_name ='blog/blog_list.html'


class BlogDetailView(DetailView):
    model=Blog
    template_name ='blog/blog_detail.html'
    login_url = 'login' 

class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model=Blog
    fields = ('title', 'body',)
    template_name ='blog/blog_edit.html'
    login_url = 'login' 

class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model=Blog
    template_name ='blog/blog_delete.html'
    success_url = reverse_lazy('blog_list')
    login_url = 'login' 

class BlogCreateView(LoginRequiredMixin, CreateView):
    model=Blog
    template_name='blog/blog_new.html'
    fields=('title', 'body')
    login_url = 'login' 

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)