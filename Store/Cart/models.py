"""Import modules"""

from django.db import models
import uuid


"""Import models"""

from Catalog.models import Catalog
from django.contrib.auth.models import User


"""Model cart"""


class Cart(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4,
        primary_key=True

    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE

    )

    completed = models.BooleanField(
        default=False

    )

    def __str__(self):
        return str(self.id)

    @property
    def total_price(self):
        cartitems = self.cartitems.all()
        total = sum([item.price for item in cartitems])
        return total


"""Model product in cart"""


class CartItem(models.Model):
    catalog = models.ForeignKey(
        Catalog,
        on_delete=models.CASCADE,
        related_name='items'

    )

    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        related_name="cartitems"

    )

    quantity = models.IntegerField(
        default=0

    )

    def __str__(self):
        return self.catalog.product_name

    @property
    def price(self):
        new_price = self.catalog.price * self.quantity
        return new_price
