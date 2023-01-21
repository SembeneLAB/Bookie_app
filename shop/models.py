from django.db import models
import datetime
from django.contrib.auth.models import User



# MODEL NAMED CATEGORY.
class Category(models.Model):
	name = models.CharField(max_length=50)

	@staticmethod
	def get_all_categories():
		return Category.objects.all()

	def __str__(self):
		return self.name
# END MODEL NAMED CATEGORY.



# MODEL NAMED CUSTOMERS.  
class Customers(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
  
    @staticmethod
    def get_all_categories():
        return Customers.objects.all()
      
    def isExists(self):
        if Customers.objects.filter(email=self.email):
            return True
  
        return False
      
    def register(self):
        self.save()
# END MODEL NAMED CUSTOMERS.        
 
 # MODEL NAMED PRODUCTS.       
class Products(models.Model):
    author = models.CharField(max_length=60, default="")
    name = models.CharField(max_length=60)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=250, default='', blank=True, null=True)
    image = models.ImageField(upload_to='uploads/products/')
  
    @staticmethod
    def get_products_by_id(ids):
        return Products.objects.filter(id__in=ids)
  
    @staticmethod
    def get_all_products():
        return Products.objects.all()
  
    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Products.objects.filter(category=category_id)
        else:
            return Products.get_all_products()

# MODEL NAMED PRODUCTS END.

# MODEL NAMED ORDERS.
class Order(models.Model):
    product = models.ForeignKey(Products,
                                on_delete=models.CASCADE)
    customer = models.ForeignKey(Customers,
                                 on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField(max_length=50, default='', blank=True)
    phone = models.CharField(max_length=50, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)
  
    def placeOrder(self):
        self.save()
  
    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer=customer_id).order_by('-date')
      
# MODEL NAMED ORDERS ENDED.
class Cart(models.Model):
    product = models.CharField(max_length=60)
    
    def __str__(self):
         return self.user.username 
    
    @staticmethod
    def get_all_product():
        return Cart.objects.all()
    
    def addCart(self):
        self.save()
        
    def __str__(self):
	    return self.product