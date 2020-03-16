from django.db import models
from django.utils import timezone


class Grade(models.Model):
    no = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)


class User(models.Model):
    uid = models.AutoField(primary_key=True)
    email = models.EmailField()
    name = models.CharField(max_length=20)
    grade = models.ForeignKey(Grade, on_delete=models.SET_DEFAULT, default=-1)
    created_at = models.DateTimeField(default=timezone.now)
    modified_at = models.DateTimeField()


class Category(models.Model):
    id = models.IntegerField(primary_key=True)
    parent = models.IntegerField()
    name = models.CharField(max_length=20)


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    cid = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, default=-1)
    created_at = models.DateTimeField(default=timezone.now)
    modified_at = models.DateTimeField()


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    pid = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    modified_at = models.DateTimeField()
