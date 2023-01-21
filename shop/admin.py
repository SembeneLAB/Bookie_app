from django.contrib import admin
from . import models

# Register MODEL CATEGORY.
class CategoryAdmin(admin.ModelAdmin):
  list_display = ("name",)

admin.site.register(models.Category, CategoryAdmin )

# Register MODEL CUSTOMERS.
class CustomersAdmin(admin.ModelAdmin):
  list_display = ("name", "email", "password", "address", "contact")
  
admin.site.register(models.Customers, CustomersAdmin)

# Register MODEL PRODUCTS.
class ProductsAdmin(admin.ModelAdmin):
  list_display = ("author", "name", "price", "category", "description", "image")
  
admin.site.register(models.Products, ProductsAdmin)

# Register MODEL ORDERS.
class OrdersAdmin(admin.ModelAdmin):
  list_display = ("product", "customer", "quantity", "price", "address", "phone", "date", "status")
  
admin.site.register(models.Order, OrdersAdmin)

# Register MODEL CATEGORY.
class CartAdmin(admin.ModelAdmin):
  list_display=("product",)

admin.site.register(models.Cart, CartAdmin )