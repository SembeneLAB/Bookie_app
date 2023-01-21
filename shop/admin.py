from django.contrib import admin
from . import models

# Register MODEL CATEGORY.
class CategoryAdmin(admin.ModelAdmin):
  list_display = ("name",)

admin.site.register(models.Category, CategoryAdmin )


# Register MODEL PRODUCTS.
class ProductsAdmin(admin.ModelAdmin):
  list_display = ("author", "name", "price", "category", "description", "image")
  
admin.site.register(models.Products, ProductsAdmin)

