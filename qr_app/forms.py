from django import forms


class TextForm(forms.Form):
    text = forms.CharField(
        widget=forms.Textarea(attrs={'id': 'qr_text_input_id',
                                     'class': 'form_text_css',
                                     'placeholder': 'Please enter the text you want to convert \nOne line per QR code'}),
        label='text', max_length=400)

    CHOICES = [('qr_code', 'Qr Code'),
               ('Code128', 'Barcode Code128'),
               ('PZN7', 'Barcode PZN7'),
               ('EAN13', 'Barcode EAN13 '),
               ('EAN14', 'Barcode EAN14'),
               ('JAN', 'Barcode JAN'),
               ('UPCA', 'Barcode UPCA'),
               ('ISBN13', 'Barcode ISBN13'),
               ('ISBN10', 'Barcode ISBN10'),
               ('ISSN', 'Barcode ISSN'),
               ('Code39', 'Barcode Code39'),
               ('PZN', 'Barcode PZN'),
               ('ITF', 'Barcode ITF'),
               ('Gs1_128', 'Barcode Gs1_128'),
               ('CODABAR', 'Barcode CODABAR')]

    barcode_type_selection = forms.ChoiceField(
        choices=CHOICES, widget=forms.Select(attrs={'id': 'qr_type_radio_input_id',
                                                    'class': 'barcode_type_css'}))
