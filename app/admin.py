from django.contrib import admin

from app.models import Cart, Contact, Product, User

# Register your models here
admin.site.register(User)
admin.site.register(Product)
admin.site.register(Contact)
admin.site.register(Cart)
