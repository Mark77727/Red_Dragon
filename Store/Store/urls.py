"""import module"""


from django.contrib import admin
from django.urls import path


"""import view"""


from Catalog.views import index
from Catalog.views import base
from Catalog.views import catalog
from Catalog.views import cpu
from Catalog.views import graphiccard
from Account.views import RegisterUser
from Account.views import AuthenticationUser
from Account.views import profile
from Account.views import orders
from Account.views import logout_view
from Cart.views import cart
from Cart import views



"""definition URL"""


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='main'),
    path('base.html', base, name='base'),
    path('catalog.html', catalog, name='catalog'),
    path('cpu.html', cpu, name='cpu'),
    path('graphiccard.html', graphiccard, name='graphiccard'),
    path('login.html', AuthenticationUser.as_view(), name='login'),
    path('logout.html', logout_view, name='logout'),
    path('login.html/sign-up.html', RegisterUser.as_view(), name='sign_up'),
    path('profile.html', profile, name='profile'),
    path('orders.html', orders, name='orders'),
    path('cart.html', cart, name='cart'),
    path('add_to_cart', views.add_to_cart, name='add')
]
