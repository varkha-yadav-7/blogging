from django import forms 
from .models import Posts
  
class PostForm(forms.Form):
    image=forms.ImageField()
    capt=forms.CharField(max_length=1000)