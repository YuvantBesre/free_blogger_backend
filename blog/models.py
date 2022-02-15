from django.db import models
from accounts.models import User

class Blog(models.Model):
    title = models.CharField(max_length=10000)
    description = models.TextField()
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_poster")
    modified = models.DateTimeField(auto_now=True, auto_now_add=False)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        ordering = ('-created',)
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    description = models.TextField()
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="blog_post")
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comment_poster")
    modified = models.DateTimeField(auto_now=True, auto_now_add=False)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        ordering = ('-created',)
    
    def __str__(self):
        return self.description