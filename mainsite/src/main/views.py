from django.shortcuts import render
from blog.models import Post
from .models import Event

# Create your views here.

def home_page(request):
  posts = Post.objects.all().order_by("-id")[:3]
  events = Event.objects.all().order_by("-id")[:3]
  
  context = {
    "posts" : posts,
    "events" : events
  }
  return render(request, 'main/index.html', context)


def about_page(request):
  
  return render(request, 'main/about.html')


def donation_page(request):
  
  return render(request, 'main/donation.html')


def our_executives(request):
  
  return render(request, 'main/executives.html')


def programs_page(request):
  
  return render(request, 'main/programs.html')
