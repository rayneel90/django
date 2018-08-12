from django.shortcuts import render, HttpResponse
from .forms import UploadFileForm
# Create your views here.


def Home(request):
    form = UploadFileForm()
    if request.method=='POST':
        print(request.FILES['file'].read())
    return render(request, 'backend.html', {'form': form})