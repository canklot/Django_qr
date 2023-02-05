from django import forms

class UploadFileForm(forms.Form):
    file = forms.FileField(widget=forms.FileInput(attrs={'id': 'file_selector_id' ,'onchange':'form.submit()'}))