from django import forms


class InsertCommentForm(forms.Form):
    voice = forms.FileField(label='voice')


class GetCommentForm(forms.Form):
    lang = forms.CharField(widget=forms.Select(choices=[('fr', "fr"), ('ar', "ar"),('en', "en")]))
