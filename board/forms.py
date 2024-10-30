from django import forms
from board.models import Create, Comment

class CreateForm(forms.ModelForm):
    class Meta:
        model = Create
        fields = ['title','contents']
        labels = {'title':'제목', 'contents':'내용'}
