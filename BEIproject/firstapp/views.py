from turtle import color
from django.shortcuts import render,redirect
from django.http import HttpResponse
from numpy import where
from pandas import value_counts
from django.contrib.auth.models import User,auth
from .models import Dealer,Vehicle
from django.contrib.auth.decorators import login_required
# Create your views here
def  home(request):

    return render(request,'home.html')



def about(request):
    name='sagar kanddddeeelll'
    
    return render(request,'about.html',{'name':name})

def register(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        mobile=request.POST['mobile']
        role=request.POST['role']
        #image=request.POST['image']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                message='username already taken'
                return render(request,'register.html',{'message':message})
            elif User.objects.filter(email=email).exists():
                message='email already exists'
                return render(request,'register.html',{'message':message})
            else:
                user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save();
                dealer = Dealer(dealer =user, mobile =mobile,role=role)
                dealer.save()
                
    
                
                return render(request,'login.html')

            
    else:
        return render(request,'register.html')
    


def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)


        if user is not None:
            auth.login(request,user)  
            userselected=User.objects.get(username=username)
            userselected=userselected.id
            role=Dealer.objects.get(dealer=user)
            role=role.role
            individual=User.objects.get(username=username)
            if role=='Vendor':
                vendor=role
                return render(request,'home.html',{'userselected':userselected,'vendor':vendor,'individual':individual})
            
            else:
                role=role
                return render(request,'home.html',{'userselected':userselected,'role':role,'individual':individual})
        
        else:
            return render(request,'login.html')
    else:
        return render(request,'login.html')


def logout(request):
    auth.logout(request)
    return render(request,'home.html') 


@login_required
def vehicles(request):
    return render(request,'vehicles.html')

@login_required
def add_vehicle(request):

    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        owner=Dealer.objects.get(dealer=user)
        vehicle_no=request.POST['vehicle_no']
        vehicle_name=request.POST['vehicle_name']
        color=request.POST['color']
        owner_photo=request.FILES['owner_photo']
        vehicle_photo=request.FILES['vehicle_photo']
        driving_license=request.FILES['driving_license']
        citizenship_front=request.FILES['citizenship_front']
        citizenship_back=request.FILES['citizenship_back']
        vehicle_details=Vehicle(vehicle_no=vehicle_no,vehicle_name=vehicle_name,color=color,owner=owner,vehicle_photo=vehicle_photo,owner_photo=owner_photo,driving_license=driving_license,citizenship_front=citizenship_front,citizenship_back=citizenship_back)
        vehicle_details.save()
        return render(request,'add_vehicle.html',{'vehicle_details':vehicle_details})
    return render(request,'add_vehicle.html')


