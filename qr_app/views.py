import datetime
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
import jwt
from .models import User
from .serializer import UserSerializer
from .forms import TextForm
from .utils.pipeline_pdf import pipeline_pdf


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

# Create your views here.


class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('User not found!')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret',
                           algorithm='HS256').decode('utf-8')

        response = Response()

        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'jwt': token
        }
        return response


class UserView(APIView):

    def get(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:
            payload = jwt.decode(token, 'secret', algorithm=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)
        return Response(serializer.data)


class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success'
        }
        return response
