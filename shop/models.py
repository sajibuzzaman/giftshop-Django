from django.db import models
from django.utils.safestring import mark_safe
from mptt.models import MPTTModel, TreeForeignKey
from django.urls import reverse
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.db.models import Count, Sum, Avg, fields
from math import floor

# Create your models here.
class Category(MPTTModel):
    parent = TreeForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    title = models.CharField(max_length=200)
    keywords = models.CharField(max_length=100)
    details = models.TextField()
    slug = models.SlugField(null=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class MPTTMeta:
        order_insertion_by = ['title']

    def __str__(self):
        return self.title


class Product(models.Model):

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    keywords = models.CharField(max_length=100)
    image = models.ImageField(blank=True, upload_to='product/')
    new_price = models.DecimalField(decimal_places=2, max_digits=15, default=0)
    amount = models.IntegerField(default=0)
    discount = models.IntegerField(default=0, blank=True, null=True)
    detail = models.TextField()
    compositions = models.CharField(max_length=100, blank=True, null=True)
    Styles = models.CharField(max_length=100, blank=True, null=True)
    Properties = models.CharField(max_length=100, blank=True, null=True)
    slug = models.SlugField(null=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="{}" heights="70" width="60" />'.format(self.image.url))
    image_tag.short_description = 'Image'

    def ImageUrl(self):
        if self.image:
            return self.image.url
        else:
            return ''

    def get_absolute_url(self):
        return reverse('product-category', kwargs={'slug': self.slug})
    
    def average_review(self):
        reviews = Comment.objects.filter(
            product=self, status=True).aggregate(average=Avg('rate'))
        avg = 0
        if reviews['average'] is not None:
            avg = float(reviews['average'])
            return avg
        else:
            return avg

    def total_review(self):
        reviews = Comment.objects.filter(
            product=self, status=True).aggregate(count=Count('id'))
        cnt = 0
        if reviews['count'] is not None:
            cnt = (reviews['count'])
            return cnt

    def discount_price(self):
       
        return floor(int(self.new_price)  - ( int(self.new_price) * ( self.discount / 100) ))

class Images(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=True)
    image = models.ImageField(blank=True, upload_to='product/')

    def __str(self):
        return self.title


class Comment(models.Model):
    STATUS = (
        ('New', 'New'),
        ('True', 'True'),
        ('False', 'False'),

    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=500, blank=True)
    rate = models.IntegerField(default=1)
    ip = models.CharField(max_length=100, blank=True)
    status = models.CharField(max_length=40, choices=STATUS, default='New')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['comment', 'rate']

class Favourite(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    def price(self):
        return self.product.new_price

    def __str__(self):
        return self.product.title

class Color(models.Model):
    name = models.CharField(max_length=20)
    code = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.name

    def color_tag(self):
        if self.code is not None:
            return mark_safe('<p style="background-color:{}">Color </p>'.format(self.code))
        else:
            return ""

class Variants(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.color.name