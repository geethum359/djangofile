from django.shortcuts import render
from modelapp.models import employee
# Create your views here.
def list(request):
    emp=employee.objects.all()
    return render(request,'list.html',{"s":emp})
def form(request):
    if(request.method=='POST'):
        eid=request.POST['eid']
        n=request.POST['n']
        p=request.POST['p']
        cn=request.POST['cn']
        d=request.POST['d']
        s=request.POST['s']
        o=employee.objects.create(emp_id=eid,emp_name=n, place=p,company_name=cn,designation=d, salary=s)
        o.save()
        return list(request)
    return render(request,'form.html')
def base(request):
    return render(request,'base.html')