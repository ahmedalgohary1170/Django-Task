from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.ForeignKey(User,related_name='post_author',on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=20000)
    publish_date= models.DateTimeField(default = timezone.now)

    imag=models.ImageField(upload_to='posts',null=True,blank=True)

    def __str__(self):
        return self.title






class Comment(models.Model):
    post =models.ForeignKey(Post,related_name='comment_post',on_delete=models.CASCADE)
    user = models.CharField(max_length=50)
    comment=models.TextField(max_length=300)
    created_ad=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.post)
