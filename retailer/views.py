from django.shortcuts import render,redirect
from accounts.models import User,Profilepic
from django.urls import reverse 
from django.http import JsonResponse,HttpResponse
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime, timedelta
import os
from django.contrib.auth.hashers import check_password
from django.contrib.auth.hashers import make_password
from distributor.models import Products
from retailer.models import Bought,Orders

def iprofile(request):
    user_id = request.session.get('user_id')
    if user_id is not None:
        profile = User.objects.get(id=user_id)
        profilepic = None
        return render(request, 'profileretailer.html',{'profile':profile,'profilepic':profilepic})    


def ieditprofile(request,id):
       farmer=User.objects.get(id=id)
       return render(request,'editprofileretailer.html',{'farmer':farmer})       

def iupdateprofile(request,id):
    user=User.objects.get(id=id)
    if request.method=='POST':
            user.name=request.POST['name']
            user.address=request.POST['address']
            user.city=request.POST['city']
            user.state=request.POST['state']
            user.save()
    return redirect(('iprofile')) 


def iprofilepic(request):
        user_id = request.session.get('user_id')
        user=User.objects.get(id=user_id)
        try:
                profile=Profilepic.objects.get(user=user)
                if profile:
                        profile.profilepic=request.FILES['profilepic']
                        profile.save()
                        file_name = profile.profilepic.name
                        file_path = os.path.join(settings.MEDIA_ROOT, file_name)
                        with open(file_path, 'wb') as destination:
                                for chunk in profile.profilepic.chunks():
                                        destination.write(chunk)  
                else:
                        profilepic=request.FILES['profilepic']
                profile=Profilepic(profilepic=profilepic,user=user)
                profile.save() 
                file_name = profile.profilepic.name
                file_path = os.path.join(settings.MEDIA_ROOT, file_name)
                with open(file_path, 'wb') as destination:
                        for chunk in profile.profilepic.chunks():
                                destination.write(chunk)  
        except:                        
                print('hey')
                profilepic=request.FILES['profilepic']
                profile=Profilepic(profilepic=profilepic,user=user)
                profile.save() 
                file_name = profile.profilepic.name
                file_path = os.path.join(settings.MEDIA_ROOT, file_name)
                with open(file_path, 'wb') as destination:
                        for chunk in profile.profilepic.chunks():
                                destination.write(chunk)          
        return render(request,'profileretailer.html')


def ichangepassword(request):
    if request.method == 'POST':
        user_id = request.session.get('user_id')
        user = User.objects.get(id=user_id)
        current_password = request.POST.get('current_password')
        new_password = request.POST.get('new_password')
        confirm_new_password = request.POST.get('confirm_new_password')
        
        # Retrieve the hashed password from the database
        password_from_db = user.password
        
        if new_password == confirm_new_password:
                # Verify the current password
             if check_password(current_password, user.password):
                # Hash the new password before saving it
                hashed_password = make_password(new_password)
                user.password = hashed_password
                user.save()
                messages = 'Password successfully changed.'
             else:
                messages = 'New password and confirm password do not match.'
        else:
            messages = 'Current password is incorrect.'
        return render(request, 'profileretailer.html', {'profile': user, 'error_messages': messages})
    return render(request, 'profileretailer.html')


def distributor(request):
      distributors=User.objects.filter(role="Distributor")
      return render(request,'distributors.html',{'distributors':distributors})

def cityvisedistributor(request):
        if request.method=="POST":
                city=request.POST['city']
                distributors=User.objects.filter(role="Distributor",city=city)
        return render(request,'distributors.html',{'distributors':distributors})
        
def allproducts(request,id):
      distributor=User.objects.get(id=id)
      products=Products.objects.filter(user=distributor)
      return render(request,'allproducts.html',{'products':products})        

def productdetails(request,id):
      product=Products.objects.get(id=id)
      return render(request,'productdetails.html',{'product':product})

def buyproducts(request,owner):
      products=Bought.objects.filter(owner=owner)
      distributors=User.objects.filter(role="Distributor")
      return render(request,'buyproducts.html',{'products':products,'owner':owner,'distributors':distributors})

def boughtproducts(request, owner, id):
    if request.method == "POST":
        name = request.POST['name']
        company = request.POST['company']
        type = request.POST['type']
        price = request.POST['price']
        quantity = request.POST['quantity']
        boughtquantity = request.POST['boughtquantity']
        user_id = request.session.get('user_id')
        user = User.objects.get(id=user_id)
        product=Products.objects.get(id=id)
        bought = Bought(user=user,product=product, name=name, company=company, owner=owner, type=type, price=price, quantity=quantity, boughtquantity=boughtquantity)
        bought.save() 
        return redirect('buyproducts')
    return render(request, 'buyproducts.html')

def deleteproduct(request,id):
      product=Bought.objects.get(id=id)
      product.delete()
      return redirect('buyproducts')

def mydistributors(request):
      user_id=request.session.get('user_id')
      user=User.objects.get(id=user_id)
      distributors=Bought.objects.filter(user=user)
      return render(request,'mydistributors.html',{'distributors':distributors})


def myorder(request):
    user_id = request.session.get('user_id')
    user = User.objects.get(id=user_id)  
    orders = Bought.objects.filter(user=user)
    for order in orders:
        existing_order, created = Orders.objects.get_or_create(
            name=order.name,
            owner=order.owner,
            buyer=user.name,
            defaults={
                'quantity': order.boughtquantity,
                'price': order.price,
                'totalprice': int(order.boughtquantity) * int(order.price)
            }
        )
        if created:
            existing_order.save()
    return redirect('order')

def order(request):
      user_id=request.session.get('user_id')
      user=User.objects.get(id=user_id)
      name=user.name
      orders=Orders.objects.filter(buyer=name)
      total=0
      for order in orders:
            total+=int(order.totalprice)
      return render(request,'myorder.html',{'orders':orders,'total':total})
      
def share(request):
        user_id=request.session.get('user_id')
        user=User.objects.get(id=user_id)
        name=user.name
        orders=Orders.objects.filter(buyer=name)
        for order in orders:            
                order.ordered=True
                order.save()
        return redirect('order')


