from django import forms
from .models import TeacherHelper


class ResumeForm(forms.ModelForm):
    class Meta:
        model = TeacherHelper
        fields = ['email', 'resume_file']

    def __init__(self, *args, **kwargs):
        super(ResumeForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'email','style': 'border-color:#0f1c70; border-radius: 5px;color:#0f1c70;'})
        self.fields['resume_file'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'upload your file here','style': 'border-color:#0f1c70; border-radius: 5px;color:#0f1c70;'})
