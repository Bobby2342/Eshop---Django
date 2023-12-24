from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User 
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


from django.contrib.auth.hashers import check_password  # Import the password checking method



from django.shortcuts import get_object_or_404, render ,redirect
from django.contrib.auth.hashers import make_password  # Import the password hashing function

from app.mail import send_custom_email

from app.models import Product, User

# Create your views here.
def index(request):
    products = Product.objects.all()

    return render (request, 'index.html', {'products':products})

def loginuser(request):
 
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(email=email )
        except User.DoesNotExist:
            error_message = 'Invalid email or password.'
            return render(request, 'login.html', {'error_message': error_message})
        
        if user and check_password(password, user.password):
            request.session['user_id'] = user.id
            return redirect('index')
        else:
            error_message = 'Invalid email or password.'
            return render(request, 'login.html', {'error_message': error_message})
    else:  # Handle GET requests separately
        return render(request, 'login.html')
    
def logoutuser(request):
    if request.user.is_authenticated:
     logout(request)
    return redirect('login')

def logoption(request):
    user = request.user if request.user.is_authenticated else None
    return render(request, 'header.html', {'user':user})

def signup(request):

    if request.method == 'POST' :
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmpassowrd =request.POST.get('confirmpassword')

        if password == confirmpassowrd:
            # hashed password

            hashed_password = make_password(password)

            user = User.objects.create(name=name, email=email, password=hashed_password)
            return redirect('login')
        else:

            error_message = "Passwords don't match. Please Try again !!"
            return render(request, 'signup.html', {'error_message':error_message})

        
    


    return render(request, 'signup.html')

def cart(request):

    cart_items = request.session.get('cart', [])
    context = {'cart_items': cart_items}
    return render(request, 'cart.html', context)

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    cart_items = request.session.get('cart', [])
    for item in cart_items:
        if item['id'] == product.id:
            item['quantity'] += 1
            break
    else:
        cart_items.append({
            'id': product.id,
            'name': product.name,
            'price': float(product.price),
            'quantity': 1,
        })

    request.session['cart'] = cart_items

    # Pass cart_items to the template context
    return redirect('cart')


def remove_from_cart(request, product_id):
     if request.method == 'POST':
        product_id = request.POST.get('item_id')  # Retrieve the product ID from the form
        
        if product_id:
            cart_items = request.session.get('cart', [])
            
            # Remove the item from the cart based on the product_id
            cart_items = [item for item in cart_items if item['id'] != int(product_id)]
            
            # Update the cart in the session without the removed item
            request.session['cart'] = cart_items
            
     return redirect('cart')  # Redirect back to the cart page or another appropriate page

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
        categories = request.POST.get('categories')

        Product.objects.create(


            name=name,
            description = description,
            price = price,
            img = img,
            condition = condition,
            imgurl = imgurl,
            categories = categories,


            



        )
        return HttpResponse('sold successfully ')

    
    return render(request, 'sell.html')


def product_details (request , pk):
    product = get_object_or_404(Product, pk=pk)
    similiar_products = product.similar_products()

    return render(request, 'product_details.html', {'product':product, 'similar_products':similiar_products})


#for categories 

def laptops(request):
    laptops = Product.objects.filter(categories__contains='laptop')
    return render(request, 'laptops.html',{'laptops':laptops})

def mobiles(request ):
    mobiles = Product.objects.filter(categories__contains='mobile')
    return render(request, 'mobiles.html',{'mobiles':mobiles})



def shoes(request):
    shoes = Product.objects.filter(categories__contains='shoes')
    return render(request, 'shoes.html',{'shoes':shoes})

def instruments(request):
    instruments = Product.objects.filter(categories__contains='instrument')
    return render(request, 'instruments.html',{'instruments':instruments})


def checkout(request):

    return render (request, 'checkout.html')

def similiarproduct(request):
    laptops = Product.objects.filter(categories__contains='laptop')
    return render(request, 'product_details.html',{'laptops':laptops})


def contact (request):

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        #send email

        subject = f'Message from {name}'
        email_message = f'From: {name}\nEmail: {email}\nMessage: {message}'
        email_from = email  # Use customer's email as sender
        recipient_list = ['bgoogly0@gmail.com']  # Update with your email

        send_custom_email (subject,email_message, email_from,recipient_list)

        from django.contrib import messages
        messages.success(request, 'Your message has been sent ! ')
       

    return render ( request, 'contact.html')