from django.db.models.expressions import Exists
from django.shortcuts import render,redirect
from django.contrib import messages
from . models import Gallery, Signup 
from . forms import SignupForm,LoginForm

# Create your views here.

def index(request):
    return render(request,'index.html')


def registration(request):
    if request.method=='POST':
        f=SignupForm(request.POST)
        if f.is_valid():
            name=f.cleaned_data['Name']
            age=f.cleaned_data['Age']
            email=f.cleaned_data['Email']
            password=f.cleaned_data['Password']
            cpassword=f.cleaned_data['ConfirmPassword']
            user=Signup.objects.filter(Email=email).exists()
            if  user:
                messages.warning(request,'email exist')
                return redirect('/registration')
            elif password!=cpassword:
                messages.warning(request,'password incorrect')
                return redirect('/registration')
            else:
                tab=Signup(Name=name,Age=age,Email=email,Password=password)
                tab.save()
                return redirect('/')
    else:
        f=SignupForm()
        return render(request,'register.html',{'form':f})



def login(request):
    if request.method=='POST':
        f=LoginForm(request.POST)
        if f.is_valid():
            email=f.cleaned_data['Email']
            password=f.cleaned_data['Password']
            user=Signup.objects.get(Email=email)
            if not user:
                messages.warning(request,'user does not exist')
                return redirect('login')
            elif user.Password!=password:
                messages.warning(request,'password missmatch')
                return redirect('login')
            else:
                return redirect('/home/%s' % user.id)
    else:
        f=LoginForm()
    return render(request,'login.html',{'form':f})


def home(request,id):
    user=Signup.objects.get(id=id)
    return render(request,'home.html',{'user':user})


def gallery(request):
    data=Gallery.objects.all()
    return render(request,'gallery.html',{'data':data})

def detailes(request,id):
    user=Gallery.objects.get(id=id)
    return render(request,'detailes.html',{'data':user})