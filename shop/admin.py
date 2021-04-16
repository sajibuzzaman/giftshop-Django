from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
import admin_thumbnails
from .models import Product, Category, Comment, Images
class CategoryAdmin(DraggableMPTTAdmin):
    prepopulated_fields = {'slug': ('title',)}
    mptt_indent_field = "title"
    list_display = ('tree_actions', 'indented_title',
                    'related_products_count', 'related_products_cumulative_count')
    list_display_links = ('indented_title',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Add cumulative product count
        qs = Category.objects.add_related_count(
                qs,
                Product,
                'category',
                'products_cumulative_count',
                cumulative=True)

        # Add non cumulative product count
        qs = Category.objects.add_related_count(qs,
                 Product,
                 'category',
                 'products_count',
                 cumulative=False)
        return qs

    def related_products_count(self, instance):
        return instance.products_count
    related_products_count.short_description = 'Related products (for this specific category)'

    def related_products_cumulative_count(self, instance):
        return instance.products_cumulative_count
    related_products_cumulative_count.short_description = 'Related products (in tree)'

#for add extra image in Product
@admin_thumbnails.thumbnail('image')
class productImageInline(admin.TabularInline):
    model = Images
    readonly_fields = ('id',)
    extra = 2
    
@admin_thumbnails.thumbnail('image')    
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'updated_at', 'image_tag']
    list_filter = ['title', 'category', 'created_at']
    list_per_page = 10
    search_fields = ['title', 'new_price', 'detail']
    inlines = [productImageInline]              #for extra image field
    prepopulated_fields = {'slug': ('title',)}  #for auto generated slug


class CommentAdmin(admin.ModelAdmin):
    readonly_fields = ['product','user', 'comment','rate', 'ip']
    list_display = ['product', 'status', 'created_at', 'updated_at', 'user']
    list_filter = ['status', 'created_at']
    list_per_page = 10

# Register your models here.
admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Comment,CommentAdmin)
