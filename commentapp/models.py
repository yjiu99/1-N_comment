from user.models import CustomUser
from django.db import models
from django.conf import settings
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateField('data published')
    writer = models.CharField(null=False, max_length=15)
    body = models.TextField()

    def __str__(self):
        return self.title

class Comment(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    text = models.CharField(max_length=100)
    username = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='comments', null=True)
    date = models.DateField(null=True)

    def __str__(self):
        return self.text
