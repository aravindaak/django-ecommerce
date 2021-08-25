from django.db import models
from django.db.models.base import Model
from django.db.models.signals import pre_save, post_save

from .utils import unique_slug_generator
# Create your models here.
# Check out on how to do large file uploads https://kirr.co/e1133t

# Custom QuerySet to override and use as Product.objects.all().featured() in views
class ProductQuerySet(models.query.QuerySet):
    def featured(self):
        return self.filter(featured = True)

    def active(self):
        return self.filter(active = True)

# Defining our own manager to give our functions for the Product.objects
# can override default methods as well like below fn can be added to class
# def all():
#   return 
class ProductManager(models.Manager):
    # Overriding existing get_queryset method to return the custom queryset module ProductQuerySet
    def get_queryset(self):
        return ProductQuerySet(self.model, self._db)
    
    def all(self):
        return self.get_queryset().active()

    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id) # Product.object == self.get_queryset()
        if qs.count() == 1:
            return qs.first()
        return None

    def featured(self): #This featured() helps you do Product.objects.featured()
        return self.get_queryset().filter(featured= True)

class Product(models.Model):
    title = models.CharField(max_length=120)
    slug =  models.SlugField(blank= True, unique = True)
    desc = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10, default=0.00)
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    featured = models.BooleanField(default=False)
    active = models.BooleanField(default=True)

    objects = ProductManager()

    #used to get the absolute url when clicking on a product in list view to go to detail view
    def get_absolute_url(self):
        return "/products/{slug}/".format(slug=self.slug)

    def __str__(self) -> str:
        return self.title
    
# To be able to generate unique slug if slug not given
def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(product_pre_save_receiver, sender=Product)