from django import forms
from .models import Mission, Comment

class Ppform(forms.ModelForm):

    class Meta:
        model = Mission
        fields = ('title','content',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].label = "제목"
        self.fields['content'].label = "설명"
        
        self.fields['title'].widget.attrs.update({
            'class': 'jss_title',
            'placeholder': '제목',
        })

        self.fields['content'].widget.attrs.update({
            'class': 'jss_content_form',
        })

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)