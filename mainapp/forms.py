from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from mainapp.models import User


class PastorSignupForm(UserCreationForm):
   
    
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ( 'full_name', 'email','phone','username', 'password1', 'password2', )
        
    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_pastor = True
        if commit:
            user.save()
        return user

class ElderSignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ( 'full_name', 'email','phone','username', 'password1', 'password2', )
        
    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_elder = True
        if commit:
            user.save()
        return user

class TreasurerSignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ( 'full_name', 'email','phone','username', 'password1', 'password2', )
        
    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_treasurer = True
        if commit:
            user.save()
        return user

class GroupLeaderSignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ( 'full_name', 'email','phone','username', 'password1', 'password2', )
        
    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_group_leader = True
        if commit:
            user.save()
        return user

class ContentManagerSignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ( 'full_name', 'email','phone','username', 'password1', 'password2', )
        
    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_content_manager = True
        if commit:
            user.save()
        return user