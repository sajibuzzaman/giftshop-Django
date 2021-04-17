from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages
from .models import ShopCart, ShopingCartForm, Order, OderForm, OderProduct
from shop.models import Product
from userApp.models import UserProfile
from giftshopApp.models import Slider
from django.contrib.auth.decorators import login_required
from django.utils.crypto import get_random_string

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

@login_required(login_url='/user/login')
def OrderCart(request):
    current_user = request.user
    shoping_cart = ShopCart.objects.filter(user_id=current_user.id)
    totalamount = 0
    for rs in shoping_cart:
        totalamount += rs.quantity*rs.product.new_price
    if request.method == "POST":
        form = OderForm(request.POST, request.FILES)
        if form.is_valid():
            dat = Order()
            # get product quantity from form
            dat.first_name = form.cleaned_data['first_name']
            dat.last_name = form.cleaned_data['last_name']
            dat.address = form.cleaned_data['address']
            dat.city = form.cleaned_data['city']
            dat.phone = form.cleaned_data['phone']
            dat.country = form.cleaned_data['country']
            dat.transaction_id = form.cleaned_data['transaction_id']
            dat.transaction_image = form.cleaned_data['transaction_image']
            dat.user_id = current_user.id
            dat.total = totalamount
            dat.ip = request.META.get('REMOTE_ADDR')
            ordercode = get_random_string(5).upper()  # random cod
            dat.code = ordercode
            dat.save()

            # moving data shortcart to product cart
            for rs in shoping_cart:
                data = OderProduct()
                data.order_id = dat.id
                data.product_id = rs.product_id
                data.user_id = current_user.id
                data.quantity = rs.quantity
                data.price = rs.product.new_price
                data.amount = rs.amount
                data.save()

                product = Product.objects.get(id=rs.product_id)
                product.amount -= rs.quantity
                product.save()
            # Now remove all oder data from the shoping cart
            ShopCart.objects.filter(user_id=current_user.id).delete()
            # request.session['cart_item']=0
            messages.success(request, 'Your oder has been completed')
            slider = Slider.objects.get(default=True)

            context = {
              
                'ordercode': ordercode,
                'slider' : slider,
            }

            return render(request, 'orderApp/oder_completed.html', context)
        else:
            messages.warning(request, form.errors)
          #  return HttpResponseRedirect("/order/oder_cart")
    form = OderForm()
    profile = UserProfile.objects.get(user_id=current_user.id)
    # total_amount = 0
    # for p in shoping_cart:
    #     total_amount += p.product.new_price*p.quantity
    slider = Slider.objects.get(default=True)

    context = {
        'shoping_cart': shoping_cart,
        'totalamount': totalamount,
        'profile': profile,
        'form': form,
        'slider' : slider,
        # 'total_amount': total_amount
    }
    return render(request, 'orderApp/order_form.html', context)

@login_required(login_url='/user/login')
def Order_showing(request):
    slider = Slider.objects.get(default=True)
    current_user = request.user
    orders = Order.objects.filter(user_id=current_user.id)
    context = {
        'slider' : slider,
        'orders': orders

    }

    return render(request, 'orderApp/user_order_showing.html', context)


@login_required(login_url='/user/login')
def user_oder_details(request, id):
    slider = Slider.objects.get(default=True)
    current_user = request.user
    order = Order.objects.get(user_id=current_user.id, id=id)
    order_products = OderProduct.objects.filter(order_id=id)
    context = {

        'order': order,
        'order_products': order_products,
        'slider' : slider,

    }
    return render(request, 'orderApp/user_order_details.html', context)

@login_required(login_url='/user/login')
def Order_Product_showing(request):
    slider = Slider.objects.get(default=True)
    current_user = request.user
    order_product = OderProduct.objects.filter(user_id=current_user.id)
    context = {
        'slider' : slider,
        'order_product': order_product

    }

    return render(request, 'orderApp/OrderProducList.html', context)


@login_required(login_url='/user/login')
def useroderproduct_details(request, id):
    slider = Slider.objects.get(default=True)
    current_user = request.user
    order_product = OderProduct.objects.get(user_id=current_user.id, id=id)
    context = {
        'order_product': order_product,
        'slider' : slider,
    }
    return render(request, 'orderApp/user_order_pro_details.html', context)