from django.contrib import admin

from app.models import Product, User

# Register your models here
admin.site.register(User)
admin.site.register(Product)