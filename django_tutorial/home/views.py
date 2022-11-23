
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import Departments, Doctors
from .forms import BookingForm

# Create your views here.

def index(request):
    variables = {'n':[10,20]}
    return render(request,'about.html',variables)

def about(request):
    return render(request,'about.html')

def booking(request):
    if request.method=='POST':
        form =BookingForm(request.POST)
        if form.is_valid:
            form.save()
            return render(request, 'conform.html')
    form =BookingForm()
    dict ={
        'form':form
    }
    
    return render(request,'booking.html', dict)

def doctors(request):
    dict={
        'doctors':Doctors.objects.all()
    }
    return render(request,'doctors.html', dict)

def contact(request):
    return render(request,'contact.html')

def department(request):
    dir_dept={
        'dept':Departments.objects.all()
    }
    return render(request,'department.html',dir_dept)

def chk(request):
    if request.method=='POST':
        lst = request.POST.getlist('attendance')
        print(lst)
    return render(request,'chk.html')
