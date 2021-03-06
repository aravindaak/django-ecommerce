"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from .views import home_page,form_page, login_page, register_page

# Check https://kirr.co/plqpin (or) https://www.codingforentrepreneurs.com/blog/common-regular-expressions-for-django-urls/ for reqex for django
urlpatterns = [
    path('register/', register_page, name='register'),
    path('login/', login_page, name='login'),
    path('home/', home_page, name='home'),
    path('contact/', form_page, name='contact'),
    path('bootstrap/', TemplateView.as_view(template_name='bootstrap/example.html')),
    path('products/', include(("products.urls", "products"), namespace="products")),
    path('search/', include(("search.urls", "search"), namespace="search")),
    path('cart/', include(("carts.urls", "carts"), namespace="cart")),
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#     url_patterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#     url_patterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)