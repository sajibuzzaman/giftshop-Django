from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Setting, Slider, About, Team, ContactForm, ContactMessage
from orderApp.models import ShopCart

# Create your views here.
def home(request):
    sliders = Slider.objects.all()
    # current_user = request.user
    # cart_products = ShopCart.objects.filter(user_id=current_user.id)
    # total_amount = 0
    # for p in cart_products:
    #     total_amount+=p.product.new_price*p.quantity

    context={
        'sliders' : sliders,
        # 'cart_products' : cart_products,
        # 'total_amount' : total_amount,
    }
    return render(request,'giftshopApp/home.html', context)

def about(request):
    slider = Slider.objects.get(default=True)
    about = About.objects.get(status=True)
    team = Team.objects.all()
    context={
        'slider' : slider,
        'about' : about,
        'team' : team,
    }
    return render(request,'giftshopApp/about.html', context)


def contact(request):
    slider = Slider.objects.get(default=True)

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = ContactMessage()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, 'Your massage has been send successfully!!')

            return redirect('contact')
    
   
    context={
      'slider' : slider,
    }
    return render(request,'giftshopApp/contact.html', context)