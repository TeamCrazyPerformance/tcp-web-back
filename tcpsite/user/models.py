from django.db import models


# Create your models here.
class Grade(models.Model):
    no = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)

    class Meta:
        verbose_name = "grade"
        ordering = ['no']

    def __str__(self):
        return self.name


class User(models.Model):
    uid = models.AutoField(primary_key=True)
    email = models.EmailField()
    name = models.CharField(max_length=20)
    grade = models.ForeignKey(Grade, on_delete=models.SET_DEFAULT, default=-1)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "user"
        ordering = ['uid']

    def __str__(self):
        return self.name
