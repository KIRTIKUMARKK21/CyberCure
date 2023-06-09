from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
#from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
       
        
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
    else:
        return render(request,'login.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        if password1==password2:
             if User.objects.filter(username=username).exists():
                 messages.info(request,'Username Taken')
                 return redirect('register')
                # print('Username taken')
             elif User.objects.filter(email=email).exists():
                  messages.info(request,'email Taken')
                  return redirect('register')
                 #print('email taken')
             else:
                 user = User.objects.create_user(username=username,password=password2,email=email, first_name=first_name, last_name=last_name)
                 user.save();
                 print('User created')
                 return redirect('login')
        else:
            print('password not match')
            return redirect('register')
        #return redirect('/')
    else:
        return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')