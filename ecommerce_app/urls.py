from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.index,name='index'),
    path('usercreate/',views.usercreate,name='usercreate'),
    path('loginpage/',views.loginpage,name='loginpage'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),

    path('admin_homepage/',views.adminhome,name='adminhome'),
    path('category_page/',views.category,name='category'),
    path('add_category/',views.addcategory,name='addcategory'),
    path('product_page/',views.product,name='product'),
    path('add_product/',views.addproduct,name='addproduct'),
    path('show_products/',views.showprdt,name='showprdt'),
    path('editproduct/<int:pk>',views.editproduct,name='editproduct'),
    path('update/<int:pk>',views.update,name='update'),
    path('delete_product/<int:pk>',views.deleteprdt,name='deleteprdt'),
    path('show_users/',views.showusr,name='showusr'),
    path('delete_user/<int:pk>',views.deleteusr,name='deleteusr'),

    path('user_homepage/',views.userhome,name='userhome'),
    path('profile/',views.profile,name='profile'),
    path('edit_profile/',views.editpage,name='editpage'),
    path('edit_details/<int:pk>',views.editdetails,name='editdetails'),
    path('addcart/<int:pk>',views.addcart,name='addcart'),
    path('cart_page/',views.cart,name='cart'),
    path('delete_item/<int:pk>',views.deleteitem,name='deleteitem'),
]