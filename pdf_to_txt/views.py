from django.shortcuts import render
from django.http import HttpResponse
from .forms import UploadFileForm
import fitz
from .utils.fitzclimc import gettext
import io


# Create your views here.
def index(request):
    if request.method != 'POST':
        form = UploadFileForm()
        return render(request, 'pdf_to_txt/form.html', {'form': form})
    form = UploadFileForm(request.POST , request.FILES)
    if form.is_valid():
        uploaded_file = form.cleaned_data['file']
        return HttpResponse( handle_uploaded_file(uploaded_file))

def handle_uploaded_file(file_to_handle):
    memory_file = io.BytesIO()
    gettext("./pdf_to_txt/utils/3page.pdf" ,memory_file)
    return_me = memory_file.getvalue()
    return return_me
    