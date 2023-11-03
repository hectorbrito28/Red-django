from django import forms

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User

from django.contrib.auth import get_user_model

from .models import Task


user = get_user_model()


class UserFormsignup(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(),label="Password")
    password2 = forms.CharField(widget=forms.PasswordInput(),label="Password verification")
    
    class Meta:
        model = user
        fields = ["username","password1","password2"]
        help_texts = {k:"" for k in fields}


class TaskForm(forms.Form):
    name = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea())



class Taskform2(forms.ModelForm):
    
    description = forms.CharField(widget=forms.Textarea())
    
    class Meta:
        model = Task
        fields = ["name","description",]
        widgets = {
            "name":forms.TextInput(attrs={"class":"form-control","placeholder":"Write title"}),
            "description":forms.Textarea(attrs={"class":"form-control","placeholder":"Write content"})
        }