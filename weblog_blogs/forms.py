from .models import Comment
from django import forms

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'نام'})

        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'ایمیل'})

        self.fields['body'].widget.attrs.update({'class': 'form-control', 'placeholder': 'پیغام'})


