from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView,DetailView
from .models import Post,About
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy

class BlogView(ListView):
    template_name = 'home.html'
    model = Post

class About(ListView):
    template_name ='about.html'
    model = About

class Detail(DetailView):
    template_name = 'detail_view.html'
    model = Post    

class NewPost(CreateView):
    template_name = 'post_new.html'
    model = Post
    fields = '__all__'
class UpdateBlog(UpdateView):
    template_name = 'update.html'
    model = Post
    fields = ['title','body']
class DeletePost(DeleteView):
    model = Post
    template_name = 'delete.html'
    success_url = reverse_lazy('home')