from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Category, Product, Cart_item
from django.contrib import messages
from django.contrib.auth.models import User, auth
import datetime

# Create your views here.

"""
names= [
        {'id': 1, 'name': 'Dharma Raj Poudel'},
        {'id': 2, 'name': 'Raju KC'},
        {'id': 3, 'name': 'Sushan Shrestha'},
    ]
"""
names = Category.objects.all()


def addtocart(request):
    if request.method=='POST':

        userid=request.POST['userid']
        product_id=int(request.POST['productid'])
        productname=str(request.POST['productname'])
        Price=float(request.POST['price'])
        quantity=float(request.POST['quantity'])
        total=quantity * Price
        status = 1
        created_at=datetime.datetime.now()
        updated_at=datetime.datetime.now()
        Cart = Cart_item(userid=userid, product_id_id=product_id, productname=productname, Price=Price, quantity=quantity, total=total, status=status, created_at=created_at, updated_at=updated_at)
        print(Cart_item)
        Cart.save()
        messages.info(request, 'Username Taken')
        return redirect('cartitems', pk=userid)
        #return render (request, 'cartitems.html', {'names':names})
    
    else:
        return redirect('/frontend')



def index(request):
    recent_product=Product.objects.all().order_by('-id').values()[:5]
    template = loader.get_template('myfirst.html')
    return HttpResponse(template.render({'names':names, 'recent_product':recent_product}))
    #return HttpResponse("Hello World!")

def about(request):
    return render(request,'about.html',{'names':names})
    #return HttpResponse("This is about!")

def cartitems(request, pk):
    CartItems = Cart_item.objects.raw("SELECT * FROM frontend_cart_item WHERE userid=%s ",[pk])
    template = loader.get_template('cartitems.html')
    return HttpResponse(template.render({'names':names, 'CartItems':CartItems}))

    #render(request,'cartitems.html' ,{'names':names, 'CartItems':CartItems})
    #return HttpResponse("This is about!")

def menu(request):
    return render(request,'navbar.html',{'names':names})


def listcategory(request, pk):
    #ProductList = Product.objects.filter(categoryid=pk)
    ProductList = Product.objects.raw("SELECT * FROM frontend_product WHERE categoryid_id=%s ",[pk])
    print(ProductList.query)
    print("----------")
    """ print(ProductList.queries)"""
    return render (request, 'listcategory.html', {'names':names, 'ProductList':ProductList})
    #SELECT * FROM Product WHERE categoryid = 1

def register(request):

    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        email=request.POST['email']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                print("Username Taken")
            elif User.objects.filter(email=email).exists():
                print("Email Taken")
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                print("User Created")
               
        else:
            print("Password not Match")
        return redirect('/frontend')
    else:
        return render(request, 'register.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return render(request, 'myfirst.html', {'names':names})
            
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return render(request, 'login.html')


def remove(self, product):
    """
    Remove a product from the cart.
    """
    product_id = str(product.id)
    if product_id in self.cart:
        # Subtract 1 from the quantity
        self.cart[product_id]['quantity'] -= 1
        # If the quantity is now 0, then delete the item
        if self.cart[product_id]['quantity'] == 0:
            del self.cart[product_id]
        self.save()
    

    
