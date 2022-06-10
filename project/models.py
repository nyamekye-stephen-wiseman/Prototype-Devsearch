from contextlib import nullcontext
from email.policy import default
from pyexpat import model
from django.db import models
import uuid
from users.models import Profile
from django.forms import UUIDField


VOTE_CHOICE = (
    ('up', 'Up Vote'),
    ('dw', 'Down Vote')
)


class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey(Profile, on_delete=models.SET_NULL, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now=True)
    modification_date = models.DateTimeField(auto_now_add=True)
    project_img = models.ImageField(default="default.jpg", blank=True, null=True)
    source_code_url = models.CharField(max_length=500, blank=True, null=True)
    demo_code_url = models.CharField(max_length=500, blank=True, null=True)
    vote_total = models.IntegerField(default=0, blank=True, null=True)
    vote_ratio = models.IntegerField(default=0, blank=True, null=True)
    tags = models.ManyToManyField('Tags')


    def __str__(self):
        return self.name

class Review(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  
    project = models.ForeignKey(Project, on_delete=models.CASCADE, blank=True, null=True)  
    up_vote = models.CharField(max_length=2, choices=VOTE_CHOICE, blank=True, null=True)
    down_vote = models.CharField(max_length=2, choices=VOTE_CHOICE, blank=True, null=True)
    created_date = models.DateTimeField(auto_now=True)
    modification_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.project.name


class Tags(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200, blank=True, null=True)
    created_date = models.DateTimeField(auto_now=True)
    modification_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    