from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from django.urls import reverse_lazy 
from .models import Post 

class PostListView(ListView):
    model = Post
    template_name = "posts/list.html"

class PostDetailView(DetailView):
    model = Post
    template_name = "posts/detail.html"

class PostCreateView(CreateView):
    model = Post
    template_name = "posts/create.html"
    fields = ["title", "subtitle", "body", "author", "status"
    ]

class PostUpdateView(UpdateView):
    template_name = "posts/edit.html"
    model = Post
    fields = ["title", "subtitle", "body", "author", "status"
    ]

class PostDeleteView(DeleteView):
    template_name = "posts/delete.html"
    model = Post
    success_url = reverse_lazy("list")
