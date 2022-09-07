from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from rest_framework.decorators import api_view
import rest_framework.response
import json

from .forms import TextForm
from .utils.barcode_logic import convert_list_to_barcode, convert_list_to_qr

max_char_limit = 20


def index(request):
    if request.method != 'POST':
        form = TextForm()
        return render(request, 'qr_app/home.html', {'form': form})

    form = TextForm(request.POST)
    if form.is_valid():
        text = form.cleaned_data['text']
        barcode_type = form.cleaned_data['barcode_type_selection']
        lines = text.splitlines()
        return pipeline_pdf(lines, barcode_type)


def pipeline_pdf(lines, barcode_type):
    if not length_valid(lines):
        return HttpResponse(f"Max character limit is {max_char_limit}")
    try:
        pdf = creator_pdf(barcode_type, lines)
    except ValueError:
        return HttpResponse("Barcode code 128 only accepts ascii character")
    return reponse_creator_pdf(pdf, barcode_type)


def creator_pdf(barcode_type, lines):
    if barcode_type == 'qr_code':
        return convert_list_to_qr(lines)
    elif barcode_type == 'barcode_code128':
        for line in lines:
            if not line.isascii():
                raise ValueError('Non ascii not supported')
        return convert_list_to_barcode(lines)


def reponse_creator_pdf(pdf, barcode_type):
    date_time = timezone.now().strftime("%m/%d/%Y-%H:%M:%S")
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{barcode_type}-{date_time}.pdf"'
    return response


def length_valid(lines):
    for line in lines:
        if len(line) > 20:
            return False
        else:
            return True


@api_view(['POST'])
def api(request):
    data = request.data
    lines = data['text']
    barcode_type = data['barcode_type_selection']
    return pipeline_pdf(lines, barcode_type)
