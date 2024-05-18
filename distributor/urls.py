from django.urls import path
from distributor import views

urlpatterns = [
    path('profile/',views.profile,name="profile"),
    path('editprofile/<int:id>/',views.editprofile,name="editprofile"),
    path('updateprofile/<int:id>/',views.updateprofile,name="updateprofile"),
    path('profilepic/',views.profilepic,name="profilepic"),
    path('changepassword/',views.changepassword,name="changepassword"),

    path('myproducts/',views.myproducts,name="myproducts"),
    path('addproducts/',views.addproducts,name="addproducts"),
    path('editproducts/<int:id>/',views.editproducts,name="editproducts"),
    path('deleteproducts/<int:id>/',views.deleteproducts,name="deleteproducts"),

    path('myorders/',views.myorders,name="myorders"),
    path('order/<str:buyer>/',views.order,name="order"),
    path('get_notifications/<int:id>/',views.get_notifications,name="get_notifications"),
    
]