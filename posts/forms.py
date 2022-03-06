from django import forms


class CommentForm(forms.Form):
    voice = forms.FileField(label='voice')