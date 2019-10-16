from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
import datetime
import random
from django.urls import reverse

# Abstracting the User model to add flags
class User(AbstractUser):
    is_pastor = models.BooleanField(default=False)
    is_elder = models.BooleanField(default=False)
    is_treasurer = models.BooleanField(default=False)
    is_group_leader = models.BooleanField(default=False)
    is_content_manager = models.BooleanField(default=False)
    full_name = models.CharField(max_length = 100)
    phone = models.IntegerField(null = True,)
    email = models.CharField(max_length=50, null = True)
    
    
class Group(models.Model):
    name = models.CharField(max_length = 100)
    leader = models.OneToOneField(User, on_delete=models.CASCADE,related_name = 'my_group')
    def __str__(self):
        return self.name

class Collection_type(models.Model):
    name = models.CharField(max_length = 100)
    is_general = models.BooleanField(default = True)
    def __str__(self):
        return self.name

class Members(models.Model):
    first_name = models.CharField(max_length = 100)
    sirname = models.CharField(max_length = 100)
    group = models.ForeignKey(Group, default = 1, on_delete=models.CASCADE, related_name = 'my_group')
    phone = models.IntegerField()
    
    
    def __str__(self):
        return self.first_name

class Contribution(models.Model):
    cont_date = models.DateField(auto_now=False, auto_now_add=False)
    member = models.ForeignKey(Members,on_delete=models.CASCADE, related_name = 'my_contributions')
    cont_type = models.ForeignKey(Collection_type, on_delete=models.CASCADE, related_name = 'contributions')
    amount = models.IntegerField()