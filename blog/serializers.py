from rest_framework import serializers
from .models import Blog, Comment
from accounts.serializers import UserSerializer
from accounts.models import User

class BlogSerializer(serializers.ModelSerializer):
    posted_by_details = UserSerializer(read_only=True, source='posted_by')

    class Meta:
        model = Blog
        fields = [
            'id',
            'title',
            'description',
            'modified',
            'created',
            'posted_by_details'
        ]

class CommentSerializer(serializers.ModelSerializer):
    posted_by_details = UserSerializer(read_only=True, source='posted_by')
    blog = serializers.SlugRelatedField(read_only=True, slug_field = 'title')

    class Meta:
        model = Comment
        fields = [
            'id',
            'description',
            'blog',
            'posted_by_details',
            'created'
        ]