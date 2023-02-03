from django.shortcuts import render
from django.http import HttpResponse
from .forms import UploadFileForm
import fitz
from .utils.fitzclimc import gettext
import io


# Create your views here.
def index(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponse('the text is: ')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})
 
def handle_uploaded_file(file_to_handle):
    memory_file = io.BytesIO()
    