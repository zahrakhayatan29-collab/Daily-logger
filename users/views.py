from django.shortcuts import render , redirect
from django.contrib.auth import authenticate, logout , login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# Create your views here.


def register_viwe(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("users:login")
        else:
            messages.error(request,'Invalid your data!')
            return redirect('users:register')
            
    form = UserCreationForm()

    return render(request,'users/register.html',context={'form':form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password= password)
        if user :
            login(request,user)
            return redirect('/')
        else :
            messages.error(request, 'Invalid username or password!')
            return render(request,'users/login.html')
    else : 
        return render(request,'users/login.html')

@login_required
def logout_viwe(request):
    logout(request)
    return redirect('users:register')
    