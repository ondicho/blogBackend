import imp
import re
from django.shortcuts import render
from blog.models import Post
from blog.serializers import PostSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['GET','POST'])
def blogView(request):
    if request.method=='GET':
        queryset=Post.objects.all()
        posts=PostSerializer(queryset,many=True)

        return Response(posts.data)
    elif(request.method == 'POST'):
        serializers = PostSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)