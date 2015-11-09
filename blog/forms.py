from django import forms
from blog.models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = post
        fields = ('title' , 'text')
