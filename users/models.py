from distutils.command.upload import upload
from email.policy import default
import profile
from pydoc import locate
from pyexpat import model
from tkinter import N
from django.db import models
from django.contrib.auth.models import User
import uuid


class Profile(models.Model):
    id= models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    username = models.CharField(max_length=200, blank=True, null=True)
    short_intro = models.CharField(max_length=100, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now=True)
    modification_date = models.DateTimeField(auto_now_add=True)
    profile_image = models.ImageField(blank=True, null=True, upload_to="profiles", default="profiles/user-default.png")
    social_github =  models.CharField(max_length=500, blank=True, null=True)
    social_twitter =  models.CharField(max_length=500, blank=True, null=True)
    social_linkedin =  models.CharField(max_length=500, blank=True, null=True)
    social_website =  models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.name


class Skill(models.Model):
    id= models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_date =models.DateTimeField(auto_now=True)
    modification_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

