from ast import Index
import datetime

from django.db import models
from django.utils import timezone
from django.contrib import admin
from django.contrib.auth.models import User
# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now



class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

def was_published_recently(self):
    now = timezone.now()
    return now - datetime.timedelta(days=1) <= self.pub_date <= now

class Post(models.Model):
    title = models.CharField(max_length=100)
    excerpt = models.CharField(max_length=200)
    image=models.ImageField(upload_to="posts",null=True)#stvara folder unutar nekog foldera i sprema sliku tamo
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, db_index=True)
    
class Comment(models.Model):
    user_name=models.CharField(max_length=50)
    user_email=models.EmailField() 
    text=models.TextField(max_length=300)
    post=models.ForeignKey(Post,on_delete=models.CASCADE, related_name="comments")

