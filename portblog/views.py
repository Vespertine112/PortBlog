from datetime import datetime
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

# Create your views here.

def index(request):
    return render(request, 'portblog/index.html', context=None)

def resume(request):
    return render(request, 'portblog/resume.html', context=None)

def archive(request):
    return render(request, 'portblog/blog_archive.html', context=None)