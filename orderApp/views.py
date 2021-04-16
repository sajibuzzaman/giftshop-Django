from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages
from .models import ShopCart, ShopingCartForm
from giftshopApp.models import Slider

# Create your views here.
def Add_to_Shoping_cart(request, id):
    url = request.META.get('HTTP_REFERER')
    current_user = request.user
    checking = ShopCart.objects.filter(
        product_id=id, user_id=current_user.id)
    if checking:
        control = 1
    else:
        control = 0

    if request.method == "POST":
        form = ShopingCartForm(request.POST)
        if form.is_valid():
            if control == 1:
                data = ShopCart.objects.filter(
                    product_id=id, user_id=current_user.id)[0]
                data.quantity += form.cleaned_data['quantity']
                data.save()
            else:
                data = ShopCart()
                data.user_id = current_user.id
                data.product_id = id
                data.quantity = form.cleaned_data['quantity']
                data.save()
        messages.success(request, 'Your Product  has been added')
        return HttpResponseRedirect(url)
    else:
        if control == 1:
            data = ShopCart.objects.filter(
                product_id=id, user_id=current_user.id)[0]
            
            data.quantity += 1
            
            data.save()
        else:
            data = ShopCart()
            data.user_id = current_user.id
            data.product_id = id
            data.quantity = 1
            data.save()
        # messages.success(request, 'Your  product has been added')
        return HttpResponseRedirect(url)

def cart_details(request):
    slider = Slider.objects.get(default=True)
    current_user = request.user
    cart_products = ShopCart.objects.filter(user_id=current_user.id)
   
    total_amount = 0
    for p in cart_products:
        total_amount+=p.product.new_price*p.quantity
  
    context={
        'slider' : slider,
        'cart_products' : cart_products,
        'total_amount' : total_amount
    }
    return render(request, 'orderApp/cart.html', context)

def cart_delete(request,id):
    url = request.META.get('HTTP_REFERER')
    current_user = request.user
    cart_products = ShopCart.objects.filter(id=id, user_id=current_user.id)
    cart_products.delete()
    messages.warning(request, 'Your  product has been deleted.')
    return HttpResponseRedirect(url)

def cart_update(request, id):
    url = request.META.get('HTTP_REFERER')
    current_user = request.user
    cart_products = ShopCart.objects.get(id=id, user_id=current_user.id)   

    if request.method == "POST":
        form = ShopingCartForm(request.POST)
        if form.is_valid():
            data = cart_products
            data.user_id = current_user.id
            data.product_id = cart_products.product.id
            data.quantity = form.cleaned_data['quantity']
            data.save()
        messages.success(request, 'Your Product  has been Updated')
        return HttpResponseRedirect(url)