from django import forms

class TextForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea,label='text', max_length=300)