from django import forms
from .models import Subject,List

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ('title',)

