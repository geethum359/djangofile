from django.shortcuts import render
from app6.models import Employee
from app6.forms import studentform

# Create your views here.
def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def file(request):
    k=Employee.objects.all()
    return render(request,'data.html',{"s":k})
def form1(request):
    form=studentform()
    if request.method =='POST':
        form=studentform(request.POST)
        if form.is_valid():
          form.save()
          return file(request)
        else:
            form=studentform()
    return render(request,'formdata.html',{"form":form})  

 