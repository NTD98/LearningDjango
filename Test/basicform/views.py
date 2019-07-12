from django.shortcuts import render
from . import form
# Create your views here.
def index(request):
    return render(request,'basicform/index.html')

def form_view(request):
    forms = form.FormName()
    
    if request.method == 'POST':
        forms = form.FormName(request.POST)

        if forms.is_valid():
            forms.save(commit=True)
            return index(request)
    return render(request,'basicform/test_form.html',{'form':forms})