from django import forms
from .models import Post, Comment, CommentReplie

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'post_image', 'category', 'body', 'url']
    def clean(self):
        if Post.objects.filter(title=self.cleaned_data['title']).exists():
            raise forms.ValidationError('This tiltle already exist!')

class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'post_image', 'category', 'body', 'url']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']

class CommentRepliesForm(forms.ModelForm):
    class Meta:
        model = CommentReplie
        fields = ['reply']
