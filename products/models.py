from django.db import models

class Category(models.Model):
    name = models.CharField('category name', max_length=30)

    class Meta():
        db_table = 'categories'

class SubCategory(models.Model):
    name = models.CharField('subcategory name', max_length=30)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    class Meta():
        db_table = 'subcategories'

class Product(models.Model):
    name           = models.CharField('product name', max_length=30)
    price          = models.DecimalField('product price', max_digits=8, decimal_places=2)
    thumbnail_url  = models.CharField('product thumbnail URL', max_length=2000)
    is_new         = models.BooleanField('new product', null=True)
    is_sale        = models.BooleanField('on sale product', null=True)
    is_soldout     = models.BooleanField('soldout product', null=True)
    is_set         = models.BooleanField('set product', null=True)
    is_picked      = models.BooleanField('MD picked product', null=True)
    contents       = models.TextField('product contents') 
    sub_category   = models.ForeignKey('SubCategory', on_delete=models.CASCADE)
    character      = models.ForeignKey('Character', on_delete=models.CASCADE)
    discount_ratio = models.DecimalField('discount ratio', max_digits=3, decimal_places=2) 
    created_at     = models.DateTimeField(auto_now_add=True)
    updated_at     = models.DateTimeField(auto_now=True)

    class Meta():
        db_table = 'products'

class ProductRelation(models.Model):
    reference       = models.ForeignKey('Product', on_delete=models.CASCADE)
    related_product = models.ForeignKey('Product', on_delete=models.CASCADE)

    class Meta():
        db_table = 'product_relations'

class Character(models.Model):
    name      = models.CharField('character name', max_length=30)
    image_url = models.CharField('character image URL', max_length=2000)
    
    class Meta():
        db_table = 'characters'

class Review(models.Model):
    rating     = models.PositiveSmallIntegerField('review rating')
    comments   = models.TextField('review comments')
    user       = models.ForeignKey('users.User', on_delete=models.CASCADE)
    product    = models.ForeignKey('Product', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta():
        db_table = 'reviews'

class Image(models.Model):
    image_url = models.URLField('image url', max_length=2000, null=True)
    review     = models.ForeignKey('Review', on_delete=models.CASCADE)
    
    class Meta():
        db_table = 'images'

class Option(models.Model):
    name = models.CharField('option name', max_length=30)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)

    class Meta():
        db_table = 'options'

class Question(models.Model):
    comments    = models.TextField('question text')
    product     = models.ForeignKey('Product', on_delete=models.CASCADE)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)
    class Meta():
        db_table = 'questions'

class Answer(models.Model):
    comments    = models.TextField('answer text')
    question    = models.ForeignKey('Question', on_delete=models.CASCADE)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)
    class Meta():
        db_table = 'answers'