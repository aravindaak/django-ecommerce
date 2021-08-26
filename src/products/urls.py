
from django.urls import path, re_path

from .views import ProductDetailSlugView,ProductDetailView,ProductFeaturedListView, ProductFeaturedDetailView, ProductListView, product_detail_view, product_list_view

# Check https://kirr.co/plqpin (or) https://www.codingforentrepreneurs.com/blog/common-regular-expressions-for-django-urls/ for reqex for django
urlpatterns = [
    path('', ProductListView.as_view(), name= 'list'),
    # path('products-fbv/', product_list_view),
    # re_path(r'^products/(?P<pk>\d+)/$', ProductDetailView.as_view()),
    re_path(r'^(?P<slug>[\w-]+)/$', ProductDetailSlugView.as_view(), name='detail'),
    # re_path(r'^products-fbv/(?P<pk>\d+)/$', product_detail_view),
    # path('products/featured/', ProductFeaturedListView.as_view()),
    # re_path(r'^products/featured/(?P<pk>\d+)/$', ProductFeaturedDetailView.as_view()),
] 