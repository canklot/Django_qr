from io import BytesIO
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,FileResponse
from .forms import TextForm
import qrcode
from PIL import Image


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
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            img = qrcode.make(form.cleaned_data['text'])
            fomatted_img = BytesIO()
            img.save(fomatted_img, format="png")
            response = HttpResponse(fomatted_img.getvalue(),content_type='image/png')
            response['Content-Disposition'] = 'attachment; filename="output.png"'
            #img.save(response,"PNG")
            return response
           # return FileResponse(form.cleaned_data['text'])

    # if a GET (or any other method) we'll create a blank form
    else:
        form = TextForm()

    return render(request, 'qr_app/form.html', {'form': form})