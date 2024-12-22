from django.urls import path
from app.views import index, search

urlpatterns = [
  path("", index, name="index"),
  path("search/", search, name="search"),
]