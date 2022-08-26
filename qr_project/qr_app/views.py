from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, FileResponse
from .utils.barcode_logic import convert_list_to_barcode, convert_list_to_qr
from .forms import TextForm



mylist = [
    {
        "author": "Mustafa",
        "title": "Baslik",
        "content": "Hi guys welcome and bye",
    },
    {
        "author": "Mehmet",
        "title": "Baslik2",
        "content": "Veni vici vokke",
    }]


def index(request):
    context = {
        "mylist": mylist
    }
    return render(request, "qr_app/home.html", context)
    # return HttpResponse("Hello, world. You're at the polls index.")


def bathroom(request):
    if __debug__:
        return HttpResponse("You only see this mesage when debug detected")
    return render(request, "qr_app/bathroom.html", {"title": "dirty"})

        
def form(request):
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
    # if a GET (or any other method) we'll create a blank form
    else:
        form = TextForm()
        
    return render(request, 'qr_app/form.html', {'form': form})
