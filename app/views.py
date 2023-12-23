from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render ,redirect
from django.urls import reverse

from app.models import Product

# Create your views here.
def index(request):
    products = Product.objects.all()

    return render (request, 'index.html', {'products':products})

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')

def cart(request):

    cart_items = Product.objects.filter(user=request.user)
    return render (request, 'cart.html', {'cart_items':cart_items})

def product_list(request):

    products = Product.objects.all()
    return render(request , 'product.html' ,{'products':products} )

def sell(request):

    if request.method == 'POST':
        name= request.POST.get('name')
        description =request.POST.get('description')
        price = request.POST.get('price')
        img = request.FILES.get('img')
        imgurl = request.POST.get('imgurl')
        condition = request.POST.get('condition')

        Product.objects.create(


            name=name,
            description = description,
            price = price,
            img = img,
            condition = condition,
            imgurl = imgurl,


            



        )
        return HttpResponse('sold successfully ')

    
    return render(request, 'sell.html')


def product_details (request , pk):
    product = get_object_or_404(Product, pk=pk)

    return render(request, 'product_details.html', {'product':product})