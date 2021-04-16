from django import template
from ..models import Setting
from orderApp.models import ShopCart

register = template.Library()


@register.simple_tag
def setting_tag():
    return Setting.objects.get(status=True)

@register.simple_tag(takes_context=True)
def cart_tag(context):
    request = context['request']
    current_user = request.user
    return ShopCart.objects.filter(user_id=current_user.id)

@register.simple_tag(takes_context=True)
def total_tag(context):
    request = context['request']
    current_user = request.user
    cart_products = ShopCart.objects.filter(user_id=current_user.id)
    total_amount = 0
    for p in cart_products:
        total_amount+=p.product.new_price*p.quantity
    return total_amount
