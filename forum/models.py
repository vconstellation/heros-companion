from django.db import models
from django.contrib.auth.models import User
from django.utils.text import Truncator
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=20, unique=True)
    description = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def get_posts_count(self):
        return Post.objects.filter(thread__category=self).count()

    def get_last_post(self):
        return Post.objects.filter(thread__category=self).order_by('-created_at').first()


class Thread(models.Model):
    subject = models.CharField(max_length=255)
    last_updated = models.DateTimeField(auto_now_add=True)
    thread_author = models.ForeignKey(User, related_name='threads', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='threads', on_delete=models.CASCADE)
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.subject

    def get_posts_count(self):
        return Post.objects.filter(thread=self).count()

class Post(models.Model):
    message = models.TextField(max_length=4000)
    thread = models.ForeignKey(Thread, related_name='posts', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    post_author = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    updated_by = models.ForeignKey(User, null=True, related_name='+', on_delete=models.CASCADE)

    def __str__(self):
        truncated_message = Truncator(self.message)
        return truncated_message.chars(30)