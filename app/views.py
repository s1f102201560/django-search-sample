from django.shortcuts import render
from app.models import Blog

# Create your views here.

def index(request):
  template_name = "app/index.html"
  blogs = Blog.objects.all()
  context = {
    "blogs": blogs,
  }

  return render(request, template_name, context)