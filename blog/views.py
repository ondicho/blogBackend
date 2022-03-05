import imp
import re
from django.shortcuts import render
from blog.models import Post
from blog.serializers import PostSerializer
from rest_framework.response import Response
# Create your views here.


def blogView(request):
    if request.method=='GET':
        queryset=Post.objects.all()
        posts=PostSerializer(queryset)

        return Response(posts)