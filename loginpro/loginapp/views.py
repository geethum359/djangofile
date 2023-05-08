from django.shortcuts import render
from loginapp.models import sigup
from loginapp.forms import sigupform
def base(request):
    return render(request,'base.html')
def home(request):
    return render(request,'home.html')
def logins(request):
    return render(request,'logins.html')
def sigup1(request):
    form=sigupform()
    if(request.method=='POST'):
        form=sigupform(request.POST)
        if form.is_valid():
            form.save()
            return home(request)
    return render(request,'sigup.html')