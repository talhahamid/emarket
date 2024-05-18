from django.shortcuts import render,redirect
from accounts.models import User,Profilepic
from distributor.models import Products
from retailer.models import Orders,Bought
from django.urls import reverse 
from django.http import JsonResponse,HttpResponse
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime, timedelta
import os
from django.contrib.auth.hashers import check_password
from django.contrib.auth.hashers import make_password

def profile(request):
    user_id = request.session.get('user_id')
    if user_id is not None:
        profile = User.objects.get(id=user_id)
        profilepic = None
        return render(request, 'profile.html',{'profile':profile,'profilepic':profilepic})    
#     else:
#         return render(request, 'profile.html')
    
def editprofile(request,id):
       farmer=User.objects.get(id=id)
       return render(request,'editprofile.html',{'farmer':farmer})       

def updateprofile(request,id):
    user=User.objects.get(id=id)
    if request.method=='POST':
            user.name=request.POST['name']
            user.address=request.POST['address']
            user.city=request.POST['city']
            user.state=request.POST['state']
            user.save()
    return redirect(('profile')) 


def profilepic(request):
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
        return render(request,'profile.html')


def changepassword(request):
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
        return render(request, 'profile.html', {'profile': user, 'error_messages': messages})
    return render(request, 'profile.html')

def myproducts(request):
      user_id=request.session.get('user_id')
      user=User.objects.get(id=user_id)
      products=Products.objects.filter(user=user)
      return render(request,'myproducts.html',{'products':products})

def addproducts(request):
        if request.method=="POST":
                name=request.POST['name']
                type=request.POST['type']
                company=request.POST['company']
                quantity=request.POST['quantity']
                price=request.POST['price']
                image1=request.FILES.get('image1')
                image2=request.FILES.get('image2')
                image3=request.FILES.get('image3')
                user_id=request.session.get('user_id')
                user=User.objects.get(id=user_id)
                products=Products(user=user,name=name,type=type,quantity=quantity,company=company,price=price,image1=image1,image2=image2,image3=image3)
                products.save()
                file_paths = [] 
                for img in [image1, image2, image3]:
                        file_name = img.name 
                        file_path = os.path.join(settings.MEDIA_ROOT, file_name)
                        file_paths.append(file_path)  
                        with open(file_path, 'wb') as destination:
                                for chunk in img.chunks():
                                        destination.write(chunk)
                return redirect('myproducts')
        return render(request,'addproducts.html')

def deleteproducts(request,id):
      product=Products.objects.get(id=id)
      product.delete()
      return redirect('myproducts')

def editproducts(request,id):
      product=Products.objects.get(id=id)
      return render(request,'editproducts.html',{'product':product})

def updateproducts(request,id):
        product=Products.objects.get(id=id)
        if request.method=='POST':
            product.name=request.POST['name']
            product.company=request.POST['company']
            product.type=request.POST['type']
            product.quantity=request.POST['quantity']
            product.price=request.POST['price']
            product.image1=request.FileT.get('image1')
            product.image2=request.FileT.get('image2')
            product.image3=request.FileT.get('image3')
            product.save()    
            file_paths = [] 
            for img in [product.image1, product.image2, product.image3]:
                        file_name = img.name 
                        file_path = os.path.join(settings.MEDIA_ROOT, file_name)
                        file_paths.append(file_path)  
                        with open(file_path, 'wb') as destination:
                                for chunk in img.chunks():
                                        destination.write(chunk)
            return redirect('myproducts')
        

def myorders(request):
       user_id=request.session.get('user_id')
       user=User.objects.get(id=user_id)
       owner=user.name
       orders=Bought.objects.filter(owner=owner)
       return render(request,'myorders.html',{'orders':orders})
        
def get_notifications(request, id):
    if id:
        try:
            user=User.objects.get(id=id)
            owner=user.name
            orders=Bought.objects.filter(owner=owner)
            buyer=[]
            for order in orders:
                buyer.append(order.user.name)
            return JsonResponse({'orders': (buyer)})
        except ObjectDoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)
    return JsonResponse({'orders': []})

def order(request,buyer):
       orders=Orders.objects.filter(buyer=buyer) 
       total=0
       for order in orders:
            total+=int(order.totalprice)
       return render(request,'order.html',{'orders':orders,'total':total})


