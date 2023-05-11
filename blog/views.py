from django.shortcuts import render, get_object_or_404
from blog.models import Post, AboutUs

def index(request):
    news=Post.objects.all()
    return render(request,'index.html',{'posts':news})

def about(request):
    about_us = AboutUs.objects.all()
    return render(request,'about.html', {'about_us': about_us})

def post_single(request, pk):
    p=get_object_or_404(Post.objects.all(),pk=pk)
    return render(request, 'post_single.html', {'post':p})
    # Post.objects.get(pk=pk)
