from typing import Any
from django.db import models
from django.views.generic import TemplateView,ListView,CreateView
from .models import Blog,Author,Comment
from django.shortcuts import render,redirect
from .forms import CommentForm
from django.contrib.auth.decorators import login_required
from .forms import BlogForm,AuthorForm
from django.urls import reverse_lazy

    
class HomePage(TemplateView):
    template_name = 'blog/homepage.html'


class BlogCreateView(CreateView):
    model = Blog
    form_class = BlogForm
    template_name = 'blog/blog_create.html'
    success_url = reverse_lazy('blog:bloglistview')  # Update the success_url

class AuthorCreateView(CreateView):
    model = Author
    form_class = AuthorForm
    template_name = 'blog/author_create.html'
    success_url = reverse_lazy('blog:authorlistview')  # Update the success_url

    
class BlogListView(ListView):
    template_name = 'blog/bloglistpage.html'
    queryset = Blog.objects.order_by('-posted_date')
    paginate_by = 5

class BlogDetailView(ListView):
    model = Comment
    template_name = 'blog/blogdetailpage.html'

    def get_queryset(self):
        queryset = super().get_queryset().filter(blog_id = self.kwargs['pk']).order_by('commented_date')
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["context"] = Blog.objects.filter(id = self.kwargs["pk"]).first()
        return context

class AuthorDetailView(ListView):
    model = Blog
    template_name = 'blog/authordetailpage.html'
    context_object_name = 'author_detail'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(author_id=self.kwargs["pk"]).order_by('-posted_date')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["context"] = Author.objects.filter(id=self.kwargs["pk"]).first()
        return context

class AuthorListView(ListView):
    template_name = 'blog/authorlistpage.html'
    queryset = Author.objects.all()

@login_required(login_url='/accounts/login/')
def CommentPage(request,pk):
    blog = Blog.objects.filter(pk=pk).first()
    if request.method == "POST":
        form = CommentForm(request.POST) 
        if form.is_valid():
            obj = form.save(commit=False)
            obj.blog_id = blog.pk
            obj.save()

            return redirect('blog:blogdetailview',pk)
    else:
        form = CommentForm()

    context = {
        'blog_' : blog,
        'form' : form,
    }            
    return render(request,'blog/commentcreatepage.html',context)