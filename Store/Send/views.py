""" import modules """


from django.shortcuts import render
from django.core.mail import send_mail


""" Import models"""


from Account.models import UserProfile
from django.contrib.auth.models import User


""" Import form """


from Send.forms import ContactForm


""" Render user information """


def send(request):
    user_name = request.user.first_name
    user_place = request.user.last_name

    form = ContactForm(initial={'first_name': user_name, 'last_name': user_place})

    if request.method =='POST':
        message = request.POST['message']
        email = request.POST['email']


        send_mail(
            'Новый заказ!', #title
            message, #message
            'settings.EMAIL_HOST_USER', #sender
            [email],
            fail_silently=False
        )
    return render(request, '../Templates/send/send.html', {'form': form, 'user_name': user_name, 'user_place': user_place})














