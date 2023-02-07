from django.shortcuts import render
from django.http import HttpResponse
from .forms import UploadFileForm
from django.utils import timezone
from .utils.fitzclimc import gettext
import io

def index(request):
    if request.method != 'POST':
        form = UploadFileForm()
        return render(request, 'pdf_to_txt/pdf_to_txt.html', {'form': form})

    form = UploadFileForm(request.POST , request.FILES)
    if form.is_valid():
        uploaded_file = form.cleaned_data['file']
        return  handle_uploaded_file(uploaded_file.read())

def handle_uploaded_file(file_to_handle):
    memory_file = io.BytesIO()
    gettext(file_to_handle ,memory_file)
    return reponse_creator_pdf(memory_file.getvalue(), file_name="converted")

def reponse_creator_pdf(file, file_name):
    date_time = timezone.now().strftime("%m/%d/%Y-%H:%M:%S")
    response = HttpResponse(file, content_type='application/text charset=utf-8')
    response['Content-Disposition'] = f'attachment; filename="{file_name}-{date_time}.txt"'
    return response
    