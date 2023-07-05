from django import forms
from .models import Comment
from .models import Blog,Author

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_content']
        
class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content', 'author']  # Customize this based on your Blog model fields

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name','about_author']