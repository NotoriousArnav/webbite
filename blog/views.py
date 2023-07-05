from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import *

# Create your views here.
class ArticleListView(ListView):
    model =  Post
    template_name = "blog.html"

class CommentListView(ListView):
    # model = Comment
    template_name = 'comments.html'
    def get_queryset(self):
        slug = self.kwargs['slug']
        post = get_object_or_404(Post, slug=slug)
        return Comment.objects.filter(post=post)

class ArticleDetailView(DetailView):
    model = Post
    template_name = "post.html"
