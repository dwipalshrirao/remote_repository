from django.db import models

# Create your models here.
class productdata(models.Model):
	product_id=models.IntegerField()
	product_name=models.CharField(max_length=100)
	product_cost=models.IntegerField()
	product_class = models.CharField(max_length=100)
	no_of_product = models.CharField(max_length=100)
	manufacturare_date=models.DateField(max_length=100)
	expirydate=models.DateField(max_length=100)
	customer_name=models.CharField(max_length=100)
	mobile=models.BigIntegerField()
	Email=models.EmailField(max_length=100)