from django.db import models


class SendForm(models.Model):

    first_name = models.CharField(
        max_length=200
    )

    last_name = models.CharField(
        max_length=200
    )

    email = models.EmailField(
        max_length=200
    )

    phone = models.CharField(
        max_length=200
    )

    delivery_address = models.CharField(
        max_length=200
    )

    message = models.TextField(
        max_length=200
    )

    def __str__(self):
        return self.email