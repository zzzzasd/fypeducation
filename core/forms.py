from django import forms

from .models import List, Subject


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ('title',)
