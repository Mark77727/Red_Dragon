from django.contrib import admin

from Cart.models import CartItem
from Cart.models import Cart

admin.site.register(CartItem)

admin.site.register(Cart)
