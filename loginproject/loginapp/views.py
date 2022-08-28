
from lib2to3.pgen2.tokenize import generate_tokens
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import EmailMessage,send_mail
from loginproject import settings
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.utils.encoding import force_str
from django.contrib.auth import authenticate,login,logout





# Create your views here.
def home(request):
    return render(request,"index.html")
def signup(request):
    if request.method=="POST":
        username=request.POST['username']
        fname = request.POST['fname']
        lname =request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        if User.objects.filter(username=username).exists():
            messages.error(request,"User already exist! try other username....")
            return redirect('home')
        if User.objects.filter(email=email).exists():
            messages.error(request,"email already exist!....")
            return redirect('home')
        if len(username)>11:
            messages.error(request,"username must under 11 characters!....")
            return redirect('home')
        if pass1!=pass2:
            messages.error(request,"Passwoed not matched!....")
            return redirect('home')
        myuser = User.objects.create_user(username,email,pass1)
        myuser.lname=lname
        myuser.fname=fname
        myuser.save()  
        return redirect('signin')
        
        
    return render(request, "signup.html")



def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']
        
        user = authenticate(username=username, password=pass1)
        
        if user is not None:
            login(request, user)
            fname = user.first_name
            # messages.success(request, "Logged In Sucessfully!!")
            return render(request, "index.html",{"fname":fname})
        else:
            messages.error(request, "Bad Credentials!!")
            return redirect('home')
    
    return render(request, "signin.html")


def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!!")
    return redirect('home')


