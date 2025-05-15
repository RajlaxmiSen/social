from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User

def home(request):
    posts = Post.objects.all()
    return render(request, 'blog/home.html', {'posts': posts, 'title': 'Home'})

def about(request):
    return render(request, 'blog/about.html')

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted'] # newest first
    paginate_by = 5

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username')) # get the data if exists or 404
        return Post.objects.filter(author=user).order_by('-date_posted') # filter the posts by the user


class PostDetailView(DetailView):
    model = Post
    # template_name = 'blog/post_detail.html'  # <app>/<model>_<viewtype>.html
    # context_object_name = 'post'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blog/post_form.html'  # <app>/<model>_<viewtype>.html
    fields = ['title', 'content']  # fields to be used in the form
    #success_url = '/'  # redirect to home page after successful creation

    def form_valid(self, form):
        form.instance.author = self.request.user  # set the author to the current user
        return super().form_valid(form)
    

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'blog/post_form.html'  # <app>/<model>_<viewtype>.html
    fields = ['title', 'content']  # fields to be used in the form
    #success_url = '/'  # redirect to home page after successful creation

    def form_valid(self, form):
        form.instance.author = self.request.user  # set the author to the current user
        return super().form_valid(form)
    
    # check if the user is the author of the post
    # if not, redirect to the post detail page
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin,DeleteView):
    model = Post
    success_url = '/'  # redirect to home page after successful deletion
    # template_name = 'blog/post_detail.html'  # <app>/<model>_<viewtype>.html
    # context_object_name = 'post'

    # check if the user is the author of the post
    # if not, redirect to the post detail page
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    
    # def get_success_url(self):
    #     return reverse('blog-home')