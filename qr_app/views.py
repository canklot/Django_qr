from django.shortcuts import render
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from .forms import TextForm
from .utils.pipeline_pdf import pipeline_pdf
from django.http import HttpResponse

def index(request):
    domain = request.get_host()
    if domain == "www.createbarcode.tk:80":
        return create_barcode(request)
    return render(request, 'qr_app/home.html')

def create_barcode(request):
    if request.method != 'POST':
        form = TextForm()
        return render(request, 'qr_app/create_barcode.html', {'form': form})

    form = TextForm(request.POST)
    if form.is_valid():
        text = form.cleaned_data['text']
        barcode_type = form.cleaned_data['barcode_type_selection']
        lines = text.splitlines()
        return pipeline_pdf(lines, barcode_type)

@api_view(['POST'])
def api(request):
    data = request.data
    lines = data['text']
    barcode_type = data['barcode_type_selection']
    return pipeline_pdf(lines, barcode_type)

def sitemap(request):
    return render(request, template_name='qr_app/sitemap.xml')

def api_usage(request):
    supported_formats=['qr_code','Code128','PZN7','EAN13','EAN14','JAN','UPCA','ISBN13','ISBN10','ISSN','Code39','PZN','ITF','Gs1_128','CODABAR',]
    context = {
        'table_general': {'URL': 'https://django-qr.vercel.app/api',
                          'Format':	'JSON',
                          'Method':	'POST',
                          'Response':	'Binary PDF File'
                          },
                          
        'api_table_fields': [
            ['Field','Type','Restraints','Description'],
            ['text', 'List of strings', 'Max length 20 per string','Data you want to create the qr_code of'],
            ["barcode_type_selection",	"String", ', '.join(supported_formats), "The type of barcode of qr_code you want to create"]
        ],
    }

    return render(request, template_name='qr_app/api_usage.html', context=context)