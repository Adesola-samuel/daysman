from django import forms
from . models import Comment,Post

class CommentForm(forms.ModelForm):
    body = forms.Textarea
    class Meta:
        model=Comment
        fields=('post','author','body','parent')
        widgets={
            'body': forms.Textarea(attrs={'rows':5, 'cols':48,'class':'form-control input-mf','placeholder':'Comment *'}),
        }

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['body'].label = ""


class PostForm(forms.Form):
    class Meta:
        model=Post
        fields=('body','image')
        widgets={
            'body': forms.Textarea(attrs={'rows':5, 'cols':40}),
        }