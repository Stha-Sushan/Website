from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    cname = models.CharField(max_length=255, help_text = 'Enter Category Name', verbose_name='Category Name')
    Description = models.CharField(max_length=255)
    status = models.BooleanField()
    #Metadata
    class Meta:
        ordering = ['cname']

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc)."""
        return self.cname
#Create the Product Model having the following feilds
#id
#user_id
#catergory_id
#s title
#s keyword
#s description
#heading
#details
#f image
#status
#created_at
#updated_at


class Product(models.Model):
    categoryid = models.ForeignKey('Category', on_delete = models.RESTRICT, null=False)
    name = models.CharField(max_length=255,help_text = 'Enter Product Name', verbose_name='Product Name')
    Description = models.TextField()
    Price = models.DecimalField(max_digits=7, decimal_places=2)
    pimage = models.ImageField(upload_to="static/images")
    status = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    #Metadata
    class Meta:
        ordering = ['name']

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc)."""
        return self.name


class Cart_item(models.Model):
    userid = models.IntegerField()
    product_id = models.ForeignKey('Product', on_delete = models.RESTRICT, null=False)
    productname = models.CharField(max_length=255, null=True)
    Price = models.DecimalField(max_digits=7, decimal_places=2)
    quantity = models.DecimalField(max_digits=7, decimal_places=2)
    total = models.DecimalField(max_digits=7, decimal_places=2)
    status = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

class Order(models.Model):
    userid = models.IntegerField()
    product_id = models.ForeignKey('Product', on_delete = models.RESTRICT, null=False)
    Price = models.DecimalField(max_digits=7, decimal_places=2)
    quantity = models.DecimalField(max_digits=7, decimal_places=2)
    total = models.DecimalField(max_digits=7, decimal_places=2)
    payment_type = models.CharField(max_length=255,help_text = 'Enter Payment type', verbose_name='Payment Type')
    status = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

class Payment(models.Model):
    userid = models.IntegerField()
    order_id = models.ForeignKey('Order', on_delete = models.RESTRICT, null=False)
    total = models.DecimalField(max_digits=7, decimal_places=2)
    payment_type = models.CharField(max_length=255,help_text = 'Enter Payment type', verbose_name='Payment Type')
    error_code = models.IntegerField()
    status = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()