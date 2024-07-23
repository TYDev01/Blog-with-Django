from django.shortcuts import render

# Create your views here.
from .models import Post

def post_list(request):
    post = Post.published.all()
    return render(request, 'blog/post/list.xhtml', {'posts': posts})