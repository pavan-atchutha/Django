from django.shortcuts import render,redirect
from .forms import studentform
from .models import Student

# Create your views here.

def student(request):
    if request.method =="POST":
        form=studentform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/show')
    else:
        form=studentform(request.POST)
    return render(request,'student.html',{'form':form})
def show(request):
    students=Student.objects.all()
    return render(request,'show.html',{'students':students})

