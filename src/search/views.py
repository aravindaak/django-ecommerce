from django.shortcuts import render
from django.db.models import Q


from django.views.generic import ListView
from products.models import Product

class SearchProductView(ListView):
    # queryset = Product.objects.all()
    template_name = "search/view.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        q = request.GET.get('q') #Using something.get is better than something['q] because the latter throws exception when not present
        if q is not None:
            return Product.objects.search(q) #if q is present in both title, desc, then it might give twice do distinct avoids that
        return Product.objects.featured()