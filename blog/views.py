from django.shortcuts import render
from blog.models import Post, AboutUs

def index(request):
    news=Post.objects.all()
    return render(request,'index.html',{'posts':news})

def about(request):
    about_us = AboutUs.objects.all()
    return render(request,'about.html', {'about_us': about_us})

