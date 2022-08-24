from django import forms

class TextForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea,label='text', max_length=300)
    CHOICES=[('qr_code','Qr Code'),('barcode_code128','Barcode Code128')]
    barcode_type_selection = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)