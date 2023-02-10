from django.shortcuts import render, HttpResponse
from .models import Post

# Create your views here.
def BlogHome(request):
    allPosts= Post.objects.all()
    context={'allPosts': allPosts}
    return render(request, 'blog/bloghome.html', context)

def BlogPost(request, slug):
    post= Post.objects.filter(slug=slug).first()
    params= {'post':post}
    return render(request, 'blog/blogpost.html', params)