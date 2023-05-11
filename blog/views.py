from django.shortcuts import render, get_object_or_404
from blog.models import Post, AboutUs
from blog.forms import PostForm
from django.shortcuts import redirect
from django.utils import timezone
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework import mixins
from .serializers import PostSerializer
from .models import Post

class PostViewSet(GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin):
    serializer_class=PostSerializer
    queryset=Post.objects.all()

def index(request):
    news = Post.objects.all()
    return render(request, 'index.html', {'posts': news})

def about(request):
    about_us = AboutUs.objects.all()
    return render(request, 'about.html', {'about_us': about_us})

def post_single(request, pk):
    p = get_object_or_404(Post.objects.all(), pk=pk)
    return render(request, 'post_single.html', {'post': p})

def post_form(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('single', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'post_add.html', {'form': form})
