from django.shortcuts import render,redirect
from . models import *
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    category=CategoryModel.objects.all()
    product=ProductModel.objects.all()
    context={'category': category,'product':product}
    return render(request,'index.html',context)





def usercreate(request):
    if request.method=='POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        uname=request.POST['uname']
        email=request.POST['email']
        address=request.POST['address']
        mobile=request.POST['number']
        age=request.POST['age']
        state=request.POST['state']
        country=request.POST['country']
        pincode=request.POST['pin']
        gender=request.POST['gender']
        photo=request.FILES.get('photo')
        password1=request.POST['password']
        password2=request.POST['cpassword']

        if password1==password2:
            if User.objects.filter(username=uname).exists():
                messages.info(request,'Username already exists')
                return redirect('index')   
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email already exists') 
                return redirect('index')
            else:
                user=User.objects.create_user(first_name=fname,last_name=lname,username=uname,email=email,password=password1)
                user.save()

                data=User.objects.get(id=user.id)
                ext_user_data=CustomerModel(address=address,mobile=mobile,age=age,state=state,country=country,
                                            pincode=pincode,gender=gender,photo=photo,customer=data)
                ext_user_data.save()
                messages.success(request,'Profile Registered')
                return redirect('index')
        else:
            messages.info(request,'Password is not matching')
            return redirect('index')   

def loginpage(request):
    return render(request,'signin.html')


def login(request):  
    if request.method=='POST':
        username=request.POST['uname']  
        password=request.POST['pswd']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            if user.is_staff:
                auth.login(request,user)
                return redirect('adminhome')
            else:
                auth.login(request,user)
                messages.info(request,f'welcome {username}')  
                return redirect('userhome')  
        else:
            messages.warning(request,'Something wrong...')
    return render(request,'index.html')              

def logout(request):
    auth.logout(request)
    return redirect('index') 





def adminhome(request):
    return render(request,'manage/adminhome.html')

def category(request):
    return render(request,'manage/category.html')

def addcategory(request):
    if not request.user.is_staff:
        return redirect('index')
    else:
        if request.method=='POST':
            categoryname=request.POST['catagoryname']
            cat_img=request.FILES.get('cat_img')
            category=CategoryModel(category_name=categoryname,cat_img=cat_img)
            category.save()
            return redirect('adminhome')
        
def product(request):
    category=CategoryModel.objects.all()
    return render(request,'manage/product.html',{'category': category})

def addproduct(request):
    if not request.user.is_staff:
        return redirect('index')
    else:
        if request.method=='POST':
            pname=request.POST['pname']
            pdes=request.POST['pdes']
            pimage=request.FILES['pimg']
            pprice=request.POST['pprice']
            pqty=request.POST['pqty']
            select=request.POST['select']
            category=CategoryModel.objects.get(id=select)
            product=ProductModel(pname=pname,pdes=pdes,pimg=pimage,pprice=pprice,pqty=pqty,pcat=category)
            product.save()
            return redirect('showprdt')

def showprdt(request):
    if not request.user.is_staff:
        return redirect('index')
    products=ProductModel.objects.all()
    context={'products':products}
    return render(request,'manage/showproduct.html',context)   

def editproduct(request,pk):
    product=ProductModel.objects.get(id=pk)
    category=CategoryModel.objects.all()
    context={'product':product,'category':category}
    return render(request,'manage/edit.html',context) 

def update(request,pk):
        if request.method=='POST':
            product=ProductModel.objects.get(id=pk)
            old=product.pimg
            new=request.FILES.get('pimg')
            if old != None and new==None:
                product.pimg=old
            else:
                product.pimg=new
            product.pname=request.POST['pname']
            product.pdes=request.POST['pdes']
            product.pprice=request.POST['pprice']
            product.pqty=request.POST['pqty']
            
            select=request.POST.get('select')
            category=CategoryModel.objects.get(id=select)
            product.pcat=category

            product.save()
            return redirect('showprdt') 
        
def deleteprdt(request,pk):
    if not request.user.is_staff:
        return redirect('index')
    product=ProductModel.objects.get(id=pk)
    product.delete()
    return redirect('showprdt')         


def showusr(request):
    if not request.user.is_staff:
        return redirect('index')
    customers=CustomerModel.objects.all()
    context={'customers':customers}
    return render(request,'manage/showuser.html',context)

def deleteusr(request,pk):
    if not request.user.is_staff:
        return redirect('index')
    customers=CustomerModel.objects.get(id=pk)
    user_id=customers.customer.id
    user=User.objects.get(id=user_id)
    customers.delete()
    user.delete()
    return redirect('showusr')



def userhome(request):
    category=CategoryModel.objects.all()
    product=ProductModel.objects.all()
    
    context={'category': category,'product':product}
    return render(request,'user/userhome.html',context)

def profile(request):
    customer=CustomerModel.objects.get(customer=request.user)
    return render(request,'user/profile.html',{'customer':customer})

def editpage(request):
    customer=CustomerModel.objects.get(customer=request.user)
    context={'edit': customer}
    return render(request,'user/editprofile.html',context)
def editdetails(request,pk):
    if request.method=='POST':
        
        customer=CustomerModel.objects.get(id=pk)
        user_id=customer.customer.id
        user=User.objects.get(id=user_id)
        user.first_name=request.POST.get('first_name')
        user.last_name=request.POST.get('last_name')
        user.username=request.POST.get('username')
        user.email=request.POST.get('email')
        customer.gender=request.POST.get('gender')
        customer.state=request.POST.get('state')
        customer.country=request.POST.get('country')
        customer.pincode=request.POST.get('pincode')
        customer.age=request.POST.get('age')
        customer.mobile=request.POST.get('number')
        customer.address=request.POST.get('address')
        old=customer.photo
        new=request.FILES.get('files')
        if old != None and new==None:
            customer.photo=old
        else:
            customer.photo=new 
          
     

        customer.save()
        user.save()
        
        
        return redirect('profile')

@login_required(login_url='index')
def addcart(request,pk):
    user_id=request.user.id
    user=CustomerModel.objects.get(customer=user_id)
    product=ProductModel.objects.get(id=pk)
    data=CartModel(user=user,product=product)
    data.save()
    return redirect('userhome')


@login_required(login_url='index')
def cart(request):
    user_id=request.user.id
    user1=CustomerModel.objects.get(customer=user_id)
    cartitems=CartModel.objects.filter(user=user1)
    context={'cartitems': cartitems}
    return render(request,'user/cart.html',context)

def deleteitem(request,pk):
    cartitem=CartModel.objects.get(id=pk)
    cartitem.delete()
    return redirect('cart')

