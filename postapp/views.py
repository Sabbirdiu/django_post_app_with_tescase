from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from .models import Post
class HomePageView(ListView):
    template_name = 'home.html'
    model = Post
    context_object_name = 'all_post_list'