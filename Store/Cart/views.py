""" import module """


from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
import json

"""Import models"""

from Catalog.models import Catalog
from Cart.models import Cart
from Cart.models import CartItem


""" View templates cart """

@login_required(login_url='login.html')
def cart(request):

    cart = None
    cartitems = []

    if request.user.is_authenticated:

        cart, created = Cart.objects.get_or_create(user=request.user, completed=False)
        cartitems = cart.cartitems.all()

    return render(request, '../Templates/cart/cart.html', {'cart': cart, 'cartitems': cartitems})


""" View templates cart """


def add_to_cart(request):
    data = json.loads(request.body)
    product_id = data["id"]
    catalog = Catalog.objects.get(id=product_id)

    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user, completed=False)
        cartitem, created = CartItem.objects.get_or_create(cart=cart, catalog=catalog)
        cartitem.quantity += 1
        cartitem.save()
        print(cartitem)
    return JsonResponse("work", safe=False)




