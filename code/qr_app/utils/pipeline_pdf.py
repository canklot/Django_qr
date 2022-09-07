from ..utils.barcode_logic import convert_list_to_barcode, convert_list_to_qr
from django.http import HttpResponse
from django.utils import timezone

max_char_limit = 20


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
