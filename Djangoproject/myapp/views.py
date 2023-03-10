from multiprocessing import get_context
from django.shortcuts import redirect, render
from django.http import HttpResponse
from templates import*
from .models import ObjectMaster
from django import forms
#index page
def index(request):
    datas=ObjectMaster.objects.all().values()
    return render(request,"Emp_reg.html",{'data':datas})
#registration page
def registration(request):
    if request.method=='POST':
        finame=request.POST['fname']
        laname=request.POST['lname']
        emailid=request.POST['email']
        passw=request.POST['passwd']
        obj=ObjectMaster()
        obj.Firstname=finame
        obj.Lastname=laname
        obj.Email=emailid
        obj.password=passw
        obj.save()
        datas=ObjectMaster.objects.all().values()
        return render(request,"Emp_reg.html",{'data':datas})
    return render(request,"registration.html")
#update form
def update(request,id):
    udata=ObjectMaster.objects.get(id=id)
    if request.method=="POST":
        finame=request.POST['fname']
        laname=request.POST['lname']
        emailid=request.POST['email']

        udata.Firstname=finame
        udata.Lastname=laname
        udata.Email=emailid
        udata.save()
        return redirect("index")
    return render(request,"update.html",{'data':udata})
#view form
def view(request,id):
    vdata=ObjectMaster.objects.get(id=id)
    return render(request,"view.html",{'data':vdata})
#delete
def delete(request,id):
    deldata=ObjectMaster.objects.get(id=id)
    deldata.delete()
    return redirect("index")
