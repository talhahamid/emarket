from django.shortcuts import render,redirect
from .models import User
from django.contrib.auth import logout as django_logout

# Create your views here.

def index(request):
    return render(request,'index.html')

def register(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        address=request.POST['address']
        phone=request.POST['phone']
        password=request.POST['password']
        city=request.POST['city']
        state=request.POST['state']
        role=request.POST['role']
        valid_roles = ['Distributor', 'Retailer']  
        if role not in valid_roles:
            return render(request, 'register.html', {'error_message': 'Invalid role'})
        
        user=User(name=name,email=email,address=address,phone=phone,password=password,city=city,state=state,role=role)
        user.save()

        return render(request,'login.html')
    return render(request,'register.html')

    
def login(request):    
    if request.method=="POST":
        phone=request.POST['phone']
        password=request.POST['password']
        user=User.objects.get(phone=phone)
        if(user.phone==phone and user.password==password):
            if user.role == 'Distributor':
                request.session['user_id'] = user.id
                return redirect('/distributor/profile/')
            elif user.role == 'Retailer':
                request.session['user_id'] = user.id
                return redirect('/retailer/iprofile/')
    return render(request,'login.html')

def logout(request):
    django_logout(request)
    request.session.flush()
    return render(request, 'login.html')

