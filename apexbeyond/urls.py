"""
URL configuration for apexbeyond project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static


from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',views.index, name='index'),
        path('login/',views.loginuser, name='loginuser'),
            path('logout/', views.logoutuser, name='logoutuser'),
            path('header/', views.logoption, name='logoption'),


            path('signup/',views.signup, name='signup'),
                path('sell/',views.sell, name='sell'),
                     path('cart/',views.cart, name='cart'),
                      path('product_details/<int:pk>/', views.product_details, name='product_details'),
                     path('products/',views.product_list, name='products'),
        path('laptops/', views.laptops, name='laptops'),
        path('mobiles/', views.mobiles, name='mobiles'),
        path('shoes/', views.shoes, name='shoes'),
         path('instruments/', views.instruments, name='instruments'),
        path('checkout/', views.checkout, name='checkout'),
         path('contact/', views.contact, name='contact'),
        path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
        path('remove_from_cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),

        #google signin

        path('auth/', include('social_django.urls', namespace='social')),

        










              

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
