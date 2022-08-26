from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, FileResponse
from .utils.barcode_logic import convert_list_to_barcode, convert_list_to_qr
from .forms import TextForm

def index(request):
    if request.method != 'POST':
        form = TextForm()
        return render(request, 'qr_app/form.html', {'form': form})
    
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = TextForm(request.POST)
        if form.is_valid():
            lines = form.cleaned_data['text'].splitlines()
            barcode_type = form.cleaned_data["barcode_type_selection"]

            if barcode_type == "qr_code":
                pdf = convert_list_to_qr(lines)
            elif barcode_type == "barcode_code128":
                pdf = convert_list_to_barcode(lines)

            response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="output.pdf"'
            return response


def bathroom(request):
    return render(request, "qr_app/bathroom.html", {"title": "dirty"})