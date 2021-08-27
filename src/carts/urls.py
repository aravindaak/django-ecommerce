
from django.urls import path, re_path

from .views import cart_home, cart_update

# Check https://kirr.co/plqpin (or) https://www.codingforentrepreneurs.com/blog/common-regular-expressions-for-django-urls/ for reqex for django
urlpatterns = [
    path('', cart_home, name= 'home'),
    path('update', cart_update, name= 'update'),
] 