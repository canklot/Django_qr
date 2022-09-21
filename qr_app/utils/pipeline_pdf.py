from ..utils.barcode_logic import convert_list_to_barcode, convert_list_to_qr
from django.http import HttpResponse
from django.utils import timezone
from barcode.errors import BarcodeError

max_char_limit = 20


def pipeline_pdf(lines, barcode_type):
    # Remove emty string from the list
    lines = [x for x in lines if x]
    if not length_valid(lines):
        return HttpResponse(f"Max character limit is {max_char_limit}")
    try:
        pdf = creator_pdf(barcode_type, lines)
    except (BarcodeError) as barcode_exc:
        return HttpResponse(repr(barcode_exc))
    return reponse_creator_pdf(pdf, barcode_type)


def creator_pdf(barcode_type, lines):

    if barcode_type == 'qr_code':
        return convert_list_to_qr(lines)
    else:  # Check if in list later
        return convert_list_to_barcode(lines, barcode_type)


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
