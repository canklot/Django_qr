from io import BytesIO
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,FileResponse
from .barcode_logic import convert_list_to_barcode, convert_list_to_qr
from .forms import TextForm

mylist = [
    {
    "author":"Mustafa",
    "title": "Baslik",
    "content":"Hi guys welcome and bye",
    },
    {
    "author":"Mehmet",
    "title": "Baslik2",
    "content":"Veni vici vokke",
    }
    
    ]
def index(request):
    context = {
        "mylist":mylist
    }
    return render(request,"qr_app/home.html",context)
    #return HttpResponse("Hello, world. You're at the polls index.")
    
def bathroom(request):
    return render(request,"qr_app/bathroom.html",{"title":"dirty"})

def form(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = TextForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            lines = form.cleaned_data['text'].splitlines()
            #pdf = convert_list_to_qr(lines)
            pdf = convert_list_to_barcode(lines)
           
            response = HttpResponse(pdf,content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="output.pdf"'
            return response
    # if a GET (or any other method) we'll create a blank form
    else:
        form = TextForm()

    return render(request, 'qr_app/form.html', {'form': form})