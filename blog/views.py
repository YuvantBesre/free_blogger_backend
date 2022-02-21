from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import BlogSerializer, CommentSerializer
from .models import Blog, Comment
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.pagination import PageNumberPagination
from .pagination import CustomPagination
from .permissions import SelfPermission
from rest_framework.response import Response
from rest_framework import status

class CreateOrListBlog(ListCreateAPIView):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = CustomPagination

    def perform_create(self, serializer):
        serializer.save(posted_by = self.request.user)

class RetrieveOrDeleteOrUpdateBlog(RetrieveUpdateDestroyAPIView):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly, SelfPermission,)
     
class CreateOrListComment(ListCreateAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = PageNumberPagination

    def get_queryset(self, *args, **kwargs):
        return Comment.objects.filter(blog__id = self.kwargs['pk'])

    def perform_create(self, serializer):
        blog = Blog.objects.get(id = self.kwargs['pk'])
        serializer.save(blog = blog, posted_by = self.request.user)

class UpdateOrDeleteComment(RetrieveUpdateDestroyAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly, SelfPermission,)
    