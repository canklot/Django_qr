from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, FileResponse
from .utils.barcode_logic import convert_list_to_barcode, convert_list_to_qr
from .forms import TextForm


def index(request):
    max_char_limit = 20
    if request.method != 'POST':
        form = TextForm()
        return render(request, 'qr_app/home.html', {'form': form})
    
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = TextForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            
            
            lines = text.splitlines()
            
            for line in lines:
                if len(line) > 20:
                    return HttpResponse(f"Max character limit is {max_char_limit}")
            barcode_type = form.cleaned_data["barcode_type_selection"]

            if barcode_type == "qr_code":
                pdf = convert_list_to_qr(lines)
            elif barcode_type == "barcode_code128":
                if not text.isascii():
                    return HttpResponse("Barcode code 128 only accepts ascii character")
                pdf = convert_list_to_barcode(lines)

            response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="QR_codes.pdf"'
            return response


def bathroom(request):
    return render(request, "qr_app/bathroom.html", {"title": "dirty"})