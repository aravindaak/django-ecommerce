from django.conf import Settings, settings
from django.db import models

from products.models import Product
from django.db.models.signals import pre_save,  m2m_changed
User = settings.AUTH_USER_MODEL


class CartManager(models.Manager):
    def get_or_new(self, request):
        cart_id = request.session.get("cart_id")
        qs = self.get_queryset().filter(id = cart_id)
        if qs.count() == 1:
            new_obj = False
            cart = qs.first()
            # Existing session cart gets associated to user when user logs in
            if request.user.is_authenticated and cart.user is None:
                cart.user = request.user
                cart.save()
        else:
            new_obj = True
            cart = Cart.objects.new(user=request.user)
            request.session['cart_id'] = cart.id
        return cart, new_obj
    
    def new(self, user=None):
        user_obj = None
        if user is not None:
            if user.is_authenticated:
                user_obj= user
        return self.model.objects.create(user=user_obj)


class Cart(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, blank=True)
    subtotal = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    total = models.DecimalField(default=0.00, max_digits = 10, decimal_places= 2)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = CartManager()

    def __str__(self):
        return str(self.id)

# To be able to generate unique slug if slug not given
def cart_m2m_changed_receiver(sender, instance, action, *args, **kwargs):
    if action == "post_add" or action == "post_remove" or action == "post_clear":
        products = instance.products.all()
        total =0
        for x in products:
            total+=x.price
            # Below if condition is just to avoid saving multiple times cause on save this receiver fn is called many times with different action values
        if instance.subtotal != total:
            instance.subtotal = total
            instance.save()

m2m_changed.connect(cart_m2m_changed_receiver, sender=Cart.products.through)

def cart_pre_save_receiver(sender, instance, *args, **kwargs):
    if instance.subtotal > 0:
        instance.total = instance.subtotal+ 10+ 50+90
    else:
        instance.total = 0.00

pre_save.connect(cart_pre_save_receiver, sender = Cart)