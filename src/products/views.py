from django.db import models
from django.http import Http404, request
from django.db.models.query import QuerySet
from django.views.generic import ListView, DetailView
from django.shortcuts import render

from carts.models import Cart
from .models import Product, ProductManager


# Class based view
class ProductListView(ListView):
    # queryset = Product.objects.all()
    template_name = "products/list.html"

    #Can be used on the detailview as well similarly 
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     print(context)
    #     return context

    def get_queryset(self, *args, **kwargs):
        return Product.objects.all()

# Function based view
def product_list_view(request):
    queryset = Product.objects.all()
    context ={
        "object_list": queryset
    }
    return render(request, "products/list.html", context)

class ProductDetailView(DetailView):
    # queryset = Product.objects.all()
    template_name = "products/detail.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_object(self, *args, **kwargs):
        pk = self.kwargs.get('pk')
        
        instance = Product.objects.get_by_id(pk)
        if instance is None:
            raise Http404('no product exists')
        return instance

def product_detail_view(request, pk=None, *args, **kwargs):
    # try:
    #     instance = Product.objects.get(id= pk)
    # except Product.DoesNotExist:
    #     print('no product exists')
    #     raise Http404('no product exists')
    # except: 
    #     print('Huh?')
    #      (OR)

    # qs = Product.objects.filter(id =pk)
    # if qs.exists() and qs.count() == 1:
    #     instance = qs.first()
    # else:
    #     raise Http404('no product exists')
    #    (OR)
    instance = Product.objects.get_by_id(pk)
    print(instance)
    if instance is None:
        raise Http404('no product exists')

    context = {
        'object': instance
    }
    return render(request, "products/detail.html", context)


class ProductDetailSlugView(DetailView):
    queryset = Product.objects.all()
    template_name = "products/detail.html"

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        cart, is_new = Cart.objects.get_or_new(self.request)
        context['cart'] = cart
        return context
    
    def get_object(self, *args, **kwargs):
        slug = self.kwargs['slug']
        instance = Product.objects.filter(slug = slug)
        print(instance)
        if instance.count() == 0: 
            raise Http404('no product exists')
        return instance.first()

class ProductFeaturedListView(ListView):
    # queryset = Product.objects.all()
    template_name = "products/list.html"

    def get_queryset(self, *args, **kwargs):
        return Product.objects.all().featured() # This is possible because we created custom query set ProductQuerySet and overrode get_queryset in models

class ProductFeaturedDetailView(DetailView):
    queryset = Product.objects.featured()
    template_name = "products/featured_detail.html"

    # def get_queryset(self, *args, **kwargs):
    #    return Product.objects.featured()
    