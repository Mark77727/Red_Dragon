""" import module """

from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView

from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from Account.forms import EditProfile
from django.views.generic import CreateView
from django.shortcuts import render



""" import models """

from .models import UserProfile
from django.contrib.auth.models import User
from .forms import RegisterUserForm

""" View templates pages """


def login(request):
    return render(request, '../Templates/account/login.html')


"""View profile data"""

@login_required(login_url='login.html')
def profile(request):
    user_register = User.objects.filter(username=request.user)
    #user_profile = UserProfile.objects.get(author=request.user)
    profile = request.user.userprofile


    if request.method == 'POST':
        form = EditProfile(request.POST, instance=profile)
        if form.is_valid():
            form = form.save(commit=False)
            form.author = request.user
            form.save()
            return redirect('profile')
    else:
        form = EditProfile(instance=profile)

    return render(request, '../Templates/account/profile.html', {
        'form': form,
        #'user_profile': user_profile,
        'user_register': user_register,

    })

def profile_edit(request, id):
    instance = get_object_or_404(UserProfile, id=id)
    form = UserProfile(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('profile')
    return render(request, '../Templates/account/profile.html', {'form': form})




@login_required(login_url='login.html')
def orders(request):
    user_profile = UserProfile.objects.filter(author=request.user)
    return render(request, '../Templates/account/orders.html', {'user_profile': user_profile})


""" Register user form """


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = '../Templates/account/sign-up.html'
    success_url = reverse_lazy('login')


""" Authentication user form """


class AuthenticationUser(LoginView):
    form_class = AuthenticationForm
    template_name = '../Templates/account/login.html'

    def get_success_url(self):
        return reverse_lazy('profile')


""" Logout user button """


def logout_view(request):
    logout(request)
    return redirect('login')


""" Getting a specific user profile """



