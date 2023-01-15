from django.db import models


""" Import modules"""


from django.db.models.signals import post_save
from django.dispatch import receiver


""" Import models"""


from django.contrib.auth.models import User


""" 1. Entity. User profile """


class UserProfile(models.Model):
    author = models.OneToOneField(
        User,
        on_delete=models.CASCADE,

        verbose_name='Имя пользователя',
    )

    phone_number = models.CharField(
        max_length=20,
        verbose_name='Номер для связи',

    )

    home_address = models.CharField(
        max_length=150,
        verbose_name='Адрес доставки',

    )

    def __str__(self):
        return self.phone_number

    class Meta:
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профили пользователей'


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """Создание профиля пользователя при регистрации"""
    if created:
        UserProfile.objects.create(author=instance)


@receiver
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()



