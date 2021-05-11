from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=30)

    class Meta():
        db_table = 'categories'


class SubCategory(models.Model):
    name = models.CharField(max_length=30)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    class Meta():
        db_table = 'sub_categories'


class Product(models.Model):
    name           = models.CharField(max_length=30)
    price          = models.DecimalField(max_digits=8, decimal_places=2)
    thunbnail_url  = models.CharField(max_length=2000)
    is_new         = models.NullBooleanField()
    is_sale        = models.NullBooleanField()
    is_soldout     = models.NullBooleanField()
    is_set         = models.NullBooleanField()
    contents       = models.TextField() 
    is_picked      = models.BooleanField(default=True, null=True)
    created_at     = models.DateTimeField(auto_now_add=True)
    sub_category   = models.ForeignKey('SubCategory', on_delete=models.CASCADE)
    character      = models.ForeignKey('Character', on_delete=models.CASCADE)
    discount_ratio = models.DecimalField(max_digits=8, decimal_places=2) 

    class Meta():
        db_table = 'products'


class ProductProduct(models.Model):
    product1 = models.ForeignKey('Product', on_delete=models.CASCADE)
    product2 = models.ForeignKey('Product', on_delete=models.CASCADE)

    class Meta():
        db_table = 'products_products'


class Character(models.Model):
    name      = models.CharField(max_length=30)
    image_url = models.CharField(max_length=2000)
    
    class Meta():
        db_table = 'characters'


class Review(models.Model):
    rating     = models.PositiveSmallIntegerField()
    comments   = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DataTimeField(auto_now=True)
    user       = models.ForeignKey('users.User', on_delete=models.CASCADE)
    product    = models.ForeignKey('Product', on_delete=models.CASCADE)
    
    class Meta():
        db_table = 'reviews'


class Image(models.Model):
    image_blob = models.ImageField(null=True)
    review     = models.ForeignKey('Review', on_delete=models.CASCADE)
    
    class Meta():
        db_table = 'images'

class Option(models.Model):
    name1   = models.CharField(max_length=30)
    name2   = models.CharField(max_length=30)
    name3   = models.CharField(max_length=30)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)

    class Meta():
        db_table = 'options'


class Question(models.Model):
    comments = models.TextField()
    product  = models.ForeignKey('Product', on_delete=models.CASCADE)
    
    class Meta():
        db_table = 'questions'


class Answer(models.Model):
    comments = models.TextField()
    question = models.ForeignKey('Question', on_delete=models.CASCADE)

    class Meta():
        db_table = 'answers'


class OrderList(models.Model):
    quantity = models.PositiveSmallIntegerField()
    product  = models.ForeignKey('Product', on_delete_models.CASCADE)
    order    = models.ForeignKey('Order', on_delete_models.CASCADE)

    class Meta():
        db_table = 'order_lists'


class Order(models.Model):
    reciever_name = models.CharField(max_length=30)
    user          = models.ForeignKey('users.User', on_delete=models.CASCADE)
    order_status  = models.ForeignKey('OrderStatus', on_delete=models.CASCACDE)

    class Meta():
        db_table = 'orders'


class OrderStatus(models.Model):
    status = models.BooleanField()

    class Meta():
        db_table = 'order_status'









