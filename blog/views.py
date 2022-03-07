import imp
import re
from django.shortcuts import render
from blog.models import Post
from blog.serializers import PostSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework import mixins
from rest_framework import generics
# Create your views here.

@api_view(['GET','POST','DELETE'])
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
    elif(request.method == 'DELETE'):
         Post.delete()
         return Response(status=status.HTTP_204_NO_CONTENT)

class blogDetailView(mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.CreateModelMixin,
                     mixins.DestroyModelMixin,
                     generics.GenericAPIView):
   
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
