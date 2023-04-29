from django.shortcuts import render
from myapp.models import student
# Create your views here.
def list(request):
    k=student.objects.all()
    return render(request,'list.html',{"s":k})





def about(request):
    return render(request,'about.html')
def home(request):
    return render(request,'home.html')
def index(request):
    return render(request,'index.html')