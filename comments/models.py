from django.db import models
from django.contrib.auth import get_user_model
from posts.models import Post

User = get_user_model()

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    reply_to = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)