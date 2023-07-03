from django.shortcuts import redirect, render
from .forms import CreateUserForm
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request, 'secureapp/index.html')


def register(request):
    form = CreateUserForm()        
    if request.method=='POST':      
       form=CreateUserForm(request.POST)
       if form.is_valid():          
           form.save()
           return redirect("two_factor:login")
       
    context={'form':form}

    return render(request, 'secureapp/register.html',context=context)

@login_required(login_url='two_factor:login')
def dashboard(request):
    return render(request, 'secureapp/dashboard.html')


def user_logout(request):
    auth.logout(request)

    return redirect("")



