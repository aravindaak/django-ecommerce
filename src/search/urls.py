
from django.urls import path, re_path

from .views import SearchProductView

# Check https://kirr.co/plqpin (or) https://www.codingforentrepreneurs.com/blog/common-regular-expressions-for-django-urls/ for reqex for django
urlpatterns = [
    path('', SearchProductView.as_view(), name= 'query'),
] 