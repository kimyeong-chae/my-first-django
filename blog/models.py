#-*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def toString(self):
        return 'author : [{}], title : [{}], text : [{}], created_date : [{}], published_date : [{}]'.format(self.author, self.title, self.text, self.created_date, self.published_date )


class Auth(models.Model):
    name = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)

    def __str__(self):
        return self.name
