from django.shortcuts import render
from .forms import FormDataForm

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = FormDataForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'success.html')
    else:
        form = FormDataForm()
    return render(request, 'index.html', {'form':form})