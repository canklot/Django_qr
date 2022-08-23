from io import BytesIO
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,FileResponse
from .forms import TextForm
import qrcode
from PIL import Image
from .pdf_logic import convert_to_pdf


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
            
            lines = form.cleaned_data['text'].splitlines()
            
            qr_images = []
            for line in lines:
                img = qrcode.make(line)
                fomatted_img = BytesIO()
                img.save(fomatted_img, format="png")    
                fomatted_img = fomatted_img.getvalue()
                qr_images.append(fomatted_img)
            pdf = convert_to_pdf(qr_images)    
            response = HttpResponse(pdf,content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="output.pdf"'
            return response

    # if a GET (or any other method) we'll create a blank form
    else:
        form = TextForm()

    return render(request, 'qr_app/form.html', {'form': form})