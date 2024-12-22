from django.shortcuts import render
from django.http import JsonResponse
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

  blogs_data = [{'title': blog.title} for blog in blogs]
  return JsonResponse({'blogs': blogs_data})