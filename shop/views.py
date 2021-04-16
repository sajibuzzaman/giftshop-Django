from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages
from django.core.paginator import Paginator
from giftshopApp.models import Slider
from .models import Product, Images, Comment, CommentForm

# Create your views here.
def shop(request):
    slider = Slider.objects.get(default=True)
    products = Product.objects.all()
    paginator = Paginator(products, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context={
        'slider' : slider,
        'page_obj' : page_obj,
    }
    return render(request, 'shop/shop.html', context)

def product_details(request,slug):
    slider = Slider.objects.get(default=True)
    product = Product.objects.get(slug=slug)
    images = Images.objects.filter(product__slug=slug)
    comments = Comment.objects.filter(product__slug=slug, status='True').order_by('-created_at')
    context={
        'slider' : slider,
        'product' : product,
        'images' : images,
        'comments' : comments,
    }
    return render(request, 'shop/product-details.html', context)

def CommentView(request, id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        pos = CommentForm(request.POST)
        if pos.is_valid():
            data = Comment()
            data.comment = pos.cleaned_data['comment']
            data.rate = pos.cleaned_data['rate']
            data.ip = request.META.get('REMOTE_ADDR')
            data.product_id = id
            current_user = request.user
            data.user_id = current_user.id
            data.save()
            messages.success(request, 'Your informative review has been sent')
            return HttpResponseRedirect(url)
    return HttpResponseRedirect(url)