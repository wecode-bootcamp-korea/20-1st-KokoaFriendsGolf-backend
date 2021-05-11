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
    name          = models.CharField(max_length=30)
    price         = models.CharField(max_length=30)
    photo_url     = models.CharField(max_length=1000)
    new_info      = models.BooleanField(default=True, null=True)
    sale_info     = models.BooleanField(default=True, null=True)
    soldout_info  = models.BooleanField(default=True, null=True)
    set_info      = models.BooleanField(default=True, null=True)
    contents      = models.TextField()
    shipping_info = models.TextField() 
    md_pick       = models.BooleanField(default=True, null=True)
    date          = models.DateTimeField(auto_now_add=True)
    sub_category  = models.ForeignKey('SubCategory', on_delete=models.CASCADE)
    character     = models.ForeignKey('Character', on_delete=models.CASCADE) 

    class Meta():
        db_table = 'products'


class Character(models.Model):
    name      = models.CharField(max_length=30)
    photo_url = models.CharField(max_length=1000)
    
    class Meta():
        db_table = 'characters'

class Review(models.Model):
    rating     = models.PositiveSmallIntegerField()
    comments   = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DataTimeField(auto_now=True)
    user       = models.ForeignKey('user.User', on_delete=models.CASCADE)
    product    = models.ForeignKey('Product', on_delete=models.CASCADE)
    
    class Meta():
        db_table = 'reviews'

class Option(models.Model):
    name           = models.CharField(max_length=30)
    classification = models.CharField(max_length=30)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)

    class Meta():
        db_table = 'options'

class Question(models.Model):
    comments = models.TextField()
    
    class Meta():
        db_table = 'questions'
        
class Answer(models.Model):
    comments = models.TextField()
    question = models.ForeignKey('Question', on_delete=models.CASCADE)

    class Meta():
        db_table = 'answers'

class ProductInfo(models.Model):
    name         = models.CharField(max_length=30)
    product_code = models.CharField(max_length=30)
    size         = models.CharField(max_length=30)
    weight       = models.CharField(max_length=30)
    material     = models.CharField(max_length=30)
    manufacturer = models.CharField(max_length=30)
    country      = models.CharField(max_length=30)
    caution      = models.TextField()
    product      = models.ForeignKey('Product', on_delete=models.CASCADE)

    class Meta():
        db_table = 'poduct_infomations'









