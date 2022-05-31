from django.shortcuts import render

from .forms import UploadForm

def index(request):
    form = UploadForm()

    return render(request, 'document/index.html', {'form': form})