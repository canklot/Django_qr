from django import forms


class TextForm(forms.Form):
    text = forms.CharField(
        widget=forms.Textarea(attrs={'id': 'qr_text_input_id',
                                     'class': 'form_text_css',
                                     'placeholder': 'Please enter the text you want to convert \nOne line per QR code'}),
        label='text', max_length=400)

    CHOICES = [('qr_code', 'Qr Code'), ('barcode_code128', 'Barcode Code128')]

    barcode_type_selection = forms.ChoiceField(
        choices=CHOICES, widget=forms.Select(attrs={'id': 'qr_type_radio_input_id',
                                                    'class': 'barcode_type_css'}))
