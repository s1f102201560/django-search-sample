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

def search(request):
  template_name = "app/index.html"
  query = request.GET.get("query")
  if query:
    blogs = Blog.objects.all().filter(title__icontains=query) # 部分一致
    print(query)
  else:
    blogs = Blog.objects.all()

  context = {
    "blogs": blogs,
  }

  return render(request, template_name, context)