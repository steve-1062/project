from django.db import models

# Create your models here.
class farmer(models.Model):
    farmer_id=models.IntegerField(primary_key=True)
    farmer_name=models.CharField(max_length=30)
    adhaar_n0=models.PositiveBigIntegerField()
    phone_no=models.PositiveBigIntegerField()
    photo = models.ImageField(upload_to='agro\pics')
    address=models.CharField(max_length=30)
    
class manager(models.Model):
    manager_id=models.IntegerField(primary_key=True)
    first_name=models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_no=models.PositiveBigIntegerField()
    department=models.CharField(max_length=15)
    address=models.CharField(max_length=30)

class product(models.Model):
    product_id=models.IntegerField(primary_key=True)
    product_name=models.CharField(max_length=30)
    
    product_img=models.ImageField(upload_to='static\images')
    
    quantity=models.FloatField()
    price=models.FloatField()
    farmer_id=models.ForeignKey(farmer(), on_delete=models.CASCADE)
    manager_id=models.ForeignKey(manager(), on_delete=models.CASCADE)

class inventory(models.Model):
    inventory_id=models.IntegerField(primary_key=True)
    location=models.CharField(max_length=15)
    manager_id=models.ForeignKey(manager(), on_delete=models.CASCADE)

class stocks(models.Model):
    stock_id=models.IntegerField(primary_key=True)
    stock_name=models.CharField(max_length=20)
    available_quantity=models.FloatField()
    price=models.FloatField()
    inventory_id=models.ForeignKey(inventory, on_delete=models.CASCADE)
    product_id=models.ForeignKey(product, on_delete=models.CASCADE)

# class cart(models.Model):
#     cart_id=models.IntegerField()
#     amount=models.FloatField()
#     total_price=models.FloatField()
#     #customer_id=models.ForeignKey(customer, on_delete=models.CASCADE)
#     product_id=models.ForeignKey(product, on_delete=models.CASCADE)
