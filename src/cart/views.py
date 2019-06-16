from django.contrib import messages
from django.shortcuts import render_to_response,RequestContext,Http404,HttpResponseRedirect,HttpResponse
from django.core.urlresolvers import reverse

from products.models import Product
from products.views import check_product
from.models import Cart,CartItem



# Create your views here.

def cart(request):
    try:
        cart_id = request.session['cart_id']
    except:
        cart_id = False
    if cart_id:
        cart = Cart.objects.get(id=cart_id)
    else:
        cart = False
    """
    try:
        exists = CartItem.objects.get(cart=cart)
    except:
        exists = False
    """
    items = CartItem.objects.filter(cart=cart)
    if len(items)>0:
        exists = True
    else:
        exists = False
    return render_to_response("cart/view_cart.html", locals(),context_instance=RequestContext(request))


def update_cart(request,id):
    try:
        product = Product.objects.get(id=id)
    except:
        product = False
    try:
        cart_id = request.session['cart_id']
    except:
        cart_id = False
    try:
        cart = Cart.objects.get(id=cart_id)
    except Cart.DoesNotExist:
        cart = Cart()
        cart.save()
        request.session['cart_id'] = cart.id

    if product:
        new_item,created = CartItem.objects.get_or_create(cart=cart,product=product)
        if created:
            messages.success(request,'cart item added')
        else:
            new_item.delete()
            messages.success(request,'cart item removed')
        return HttpResponseRedirect(reverse('cart'))
