from django.urls import path
from retailer import views

urlpatterns = [
    path('iprofile/',views.iprofile,name="profile"),
    path('editprofile/<int:id>/',views.ieditprofile,name="editprofile"),
    path('updateprofile/<int:id>/',views.iupdateprofile,name="updateprofile"),
    path('profilepic/',views.iprofilepic,name="profilepic"),
    path('changepassword/',views.ichangepassword,name="changepassword"),

    path('distributor/',views.distributor,name="distributor"),
    path('cityvisedistributor/',views.cityvisedistributor,name="cityvisedistributor"),
    path('allproducts/<int:id>/',views.allproducts,name="allproducts"),
    path('productdetails/<int:id>/',views.productdetails,name="productdetails"),
    path('buyproducts/<str:owner>/',views.buyproducts,name="buyproducts"),
    path('boughtproducts/<str:owner>/<int:id>/',views.boughtproducts,name="boughtproducts"),
    path('deleteproduct/<int:id>/',views.deleteproduct,name="deleteproduct"),
    path('mydistributors/',views.mydistributors,name="mydistributors"),
    path('myorder/',views.myorder,name="myorder"),
    path('order/',views.order,name="order"),
    path('share/',views.share,name="share"),
]
