
from django.shortcuts import redirect, render
from .models import *
from django.contrib.auth.decorators import login_required
from .form import *
from django.contrib.auth import logout
from .form import Form_login
from django.contrib.auth import login,authenticate

from .models import *
# Create your views here.
@login_required(login_url='login')
def home(request):
      product=Product.objects.all()
      context={'product':product}
      return render(request, 'home.html',context=context)
@login_required(login_url='login')
def add(request):
    if request.method=='POST':
        nameProduct=request.POST.get('name')
        date=request.POST.get('date')
        price=request.POST.get('price')
        about=request.POST.get('desc')
        rate=request.POST.get('rate')
        slug=request.POST.get('slug')
        img=request.POST.get('img')
        
        saveProduct=Product(name=nameProduct,price=price,slug=slug,date=date,rate=rate,about=about,img=img)
        if(saveProduct is not None):

            saveProduct.save()
            return redirect("home")
    return render(request, 'forms/add.html')

def Login_user(request):
    form = Form_login()

    if request.method == 'POST':
        form = Form_login(request.POST)
        
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
                login(request, user)
                return redirect('/')  # Replace 'home' with the name of the view you want to redirect to after successful login
        else:
                form=Form_login()  # Reset the form if authentication fails

    return render(request, 'forms/login.html', {'form': form})


def logout_view(request):
    logout(request) # type: ignore
    return redirect('login')

def signup(request):
    if request.method=='POST':
        signup=UserCreationForms(request.POST)
        
        if signup.is_valid():
            signup.save()
            return redirect('login')
    else:
            signup=UserCreationForms()



    return render(request,'forms/signup.html',
                  context={'signup':signup}
                  )

def product(request):
     
     product=Product.objects.all()
     context={'product':product}

     return render(request,'product.html',context=context)
def users(request):
     
     users=User.objects.all()
     context={'users':users}
     return render(request,'user.html',context=context)

def profile(request):  
     profile=User.objects.all()
     context={'profile':profile}
     return render(request,'profile.html',context=context)


def detal_product(request,slug):
    
     detal_products=Product.objects.get(slug=slug)
     context={
        'detal_product':detal_products
    }
     return render (request,'detal_product.html',context=context)



def update(request,pk):
    products=Product.objects.get(id=pk)
    form=Product_Form(instance=products)
    if request.method=='POST':
        form=Product_Form(request.POST,instance=products)
        if form.is_valid():
            form.save()
            return redirect('/')
         
    context={
        'form':form
    }
    return render (request,'crud/update.html',context=context)


def delete(request,pk):
    deletes=Product.objects.get(id=pk)
    if request.method=='POST':
        deletes.delete()
        return redirect('/')
    contect={
        'delete':deletes
    }
    return render(request,'delete.html',context=contect)