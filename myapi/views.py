import requests
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PostSerializer
from .models import Posts

class PostViewSet(viewsets.ModelViewSet):
    # queryset = Posts.objects.all().order_by('title')
    queryset = Posts.objects.all()
    serializer_class = PostSerializer

def home(request):
    response = requests.get('http://127.0.0.1:8000/api/posts/')
    data = response.json()
    return render(request, 'home.html', {'data': data})
