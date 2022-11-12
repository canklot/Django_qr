from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
import json
import requests
from .forms import TextForm
from .utils.pipeline_pdf import pipeline_pdf

jsonlist = []


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


@api_view(['POST'])
def api(request):
    data = request.data
    lines = data['text']
    barcode_type = data['barcode_type_selection']
    return pipeline_pdf(lines, barcode_type)


def api_usage(request):
    supported_formats = ['qr_code',
                         'Code128',
                         'PZN7',
                         'EAN13',
                         'EAN14',
                         'JAN',
                         'UPCA',
                         'ISBN13',
                         'ISBN10',
                         'ISSN',
                         'Code39',
                         'PZN',
                         'ITF',
                         'Gs1_128',
                         'CODABAR', ]
    context = {
        'table_general': {'URL': 'https://django-qr.vercel.app/api',
                          'Format':	'JSON',
                          'Method':	'POST',
                          'Response':	'Binary PDF File'
                          },

        'api_table_fields': [
            ['Field',	'Type',	'Restraints',	'Description'],
            ['text', 'List of strings', 'Max length 20 per string',
                'Data you want to create the qr_code of'],
            ["barcode_type_selection",	"String", ', '.join(supported_formats),
                "The type of barcode of qr_code you want to create"]
        ],
    }

    return render(request, template_name='qr_app/api_usage.html', context=context)


def sitemap(request):
    return render(request, template_name='qr_app/sitemap.xml')


@csrf_exempt
def webhook(request):
    print("got a webhook request ")
    if request.method == "GET":
        face_secret = "attackontitans99"
        verify_token = request.GET.get('hub.verify_token', 'noverifytoken')
        challenge = request.GET.get('hub.challenge', 'nochallange')
        if face_secret == verify_token:
            print("correct token ")
            return HttpResponse(challenge)

    if request.method == "POST":
        if request.headers.get('content-type') == 'application/json':
            json_data = json.loads(request.body)

            with open("jsonlogs.json", 'a', encoding='utf-8') as f:
                f.writelines(json.dumps(json_data) + "\n")

            

        temp_ac_token = "EAAGZBco97Pm8BAIm03Y760Bp27orQjgGNLTuRo3hAcb3tq4YcImZB9CwrrfOSq4EqWFz0ZB4EqjlZBBZAvsTiitpjV2gLInAcvJeZB6vSIZBeFNMtoMX2l5JGAnYlARcx0CuclNFbjFCw4mVHj4znWTABRKxZBPxqCnk733d1Qonk9Dlvb7B4EZAwgopYgDtcOBZBl3KhwGnZAGRgZDZD"

        my_headers = {"Authorization": "Bearer" + " " + temp_ac_token,
                      "Content-Type": "application/json", }

        post_url = "https://graph.facebook.com/v15.0/102627869338297/messages"

        my_template = {
            "name": "hello_world",
            "language": {"code": "en_US"}
        }

        my_data = {
            "messaging_product": "whatsapp",
            "to": "48505122109",
            "type": "template",
            "template": my_template
        }

        jsonlist.append(json_data)
        if "messages" in json_data["entry"][0]["changes"][0]["value"]:
                message_recived = json_data["entry"][0]["changes"][0]["value"]["messages"][0]["text"]["body"]
                print(message_recived)
        else:
            message_recived = None

        if message_recived == "hi":
            json_to_send = json.dumps(my_data)
            response = requests.post(post_url, data=json_to_send, headers=my_headers)
            content = response.content
            print(content)
    # You need to return blank 200 ok mesage to sender to say I revieved the message stop sending it
    return HttpResponse("")
