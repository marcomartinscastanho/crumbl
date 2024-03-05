from rest_framework import generics
from rest_framework import permissions
from posts.models import Post, PostImage
from .serializers import PostImageSerializer, PostSerializer


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]


class PostImageList(generics.ListCreateAPIView):
    queryset = PostImage.objects.filter(post__isnull=True)
    serializer_class = PostImageSerializer
    permission_classes = [permissions.IsAuthenticated]


class PostImageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PostImage.objects.all()
    serializer_class = PostImageSerializer
    permission_classes = [permissions.IsAuthenticated]
