from django.db import models


# Create your models here.
class Category(models.Model):
    id = models.IntegerField(primary_key=True)
    parent = models.IntegerField()
    name = models.CharField(max_length=20)

    class Meta:
        verbose_name = "category"
        ordering = ['id']

    def __str__(self):
        return self.name


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey('user.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    cid = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, default=-1)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "post"
        ordering = ['id']

    def __str__(self):
        return self.title


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey('user.User', on_delete=models.CASCADE)
    content = models.TextField()
    pid = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "comment"
        ordering = ['id']

    def __str__(self):
        return self.content
