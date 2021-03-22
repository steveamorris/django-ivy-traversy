from django.contrib import admin

# Register your models here.
from .models import *
class ProductAdmin(admin.ModelAdmin):
  list_display = ('_id', 'name', 'category', 'rating', 'countInStock', 'price')
  list_display_links = ('_id', 'name')
  list_filter = ('category',)
  list_editable = ('price', 'countInStock')





admin.site.register(Product, ProductAdmin)
admin.site.register(Review)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)