from django.db import models

# Create your models here.

class Club(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField()
    motto = models.CharField(max_length = 100)
    category = models.CharField(max_length = 100)
    created_at = models.DateTimeField(auto_now_add = True)

class Member(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField()
    phone = models.CharField(max_length = 10)
    joined_at = models.DateTimeField(auto_now_add = True)
    clubs = models.ManyToManyField(Club)

class Event(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length = 100)
    club = models.ForeignKey(Club, on_delete = models.CASCADE)
    registrants = models.ManyToManyField(Member)