from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post # model that should be used to create this form
        fields = ('title', 'text',)
