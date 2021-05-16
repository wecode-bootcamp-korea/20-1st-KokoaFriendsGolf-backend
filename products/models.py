from django.db import models

class Category(models.Model):
    name = models.CharField('category name', max_length=30, unique=True)

    class Meta():
        db_table = 'categories'

class SubCategory(models.Model):
    name = models.CharField('subcategory name', max_length=30, unique=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    class Meta():
        db_table = 'subcategories'

class Product(models.Model):
    name           = models.CharField('product name', max_length=30, unique=True)
    price          = models.DecimalField('product price', max_digits=10, decimal_places=2)
    thumbnail_url  = models.CharField('product thumbnail URL', max_length=2000)
    is_new         = models.BooleanField('new product', null=True)
    is_sale        = models.BooleanField('on sale product', null=True)
    is_soldout     = models.BooleanField('soldout product', null=True)
    is_set         = models.BooleanField('set product', null=True)
    is_picked      = models.BooleanField('MD picked product', null=True)
    contents       = models.TextField('product contents') 
    subcategory    = models.ForeignKey('SubCategory', on_delete=models.CASCADE)
    character      = models.ForeignKey('Character', on_delete=models.CASCADE)
    discount_ratio = models.DecimalField('discount ratio', max_digits=3, decimal_places=2) 
    created_at     = models.DateTimeField(auto_now_add=True)
    updated_at     = models.DateTimeField(auto_now=True)

    class Meta():
        db_table = 'products'
    
    def get_info(self):
        subcategory = SubCategory.objects.get(id=self.subcategory.id)
        category = subcategory.category

        product_info = {
            "id"            : self.id,
            "name"          : self.name,
            "price"         : float(self.price),
            "thumbnail_url" : self.thumbnail_url,
            "is_new"        : False if not self.is_new else True,
            "is_sale"       : False if not self.is_sale else True,
            "is_soldout"    : False if not self.is_soldout else True,
            "is_set"        : False if not self.is_set else True,
            "is_picked"     : False if not self.is_picked else True,
            "counts_liked"  : self.like_users.count(),
            "contents"      : self.contents,
            "subcategory"   : subcategory.name,
            "category"      : category.name,
            "character"     : self.character.name,
            "discount_ratio": float(self.discount_ratio),
            "created_at"    : self.created_at.strftime("%Y-%m-%d %H:%M:%S"),
            "updated_at"    : self.updated_at.strftime("%Y-%m-%d %H:%M:%S"),
        }
        
        return product_info

class ProductRelation(models.Model):
    reference       = models.ForeignKey('Product', related_name='reference', on_delete=models.CASCADE)
    related_product = models.ForeignKey('Product', related_name='related_products', on_delete=models.CASCADE)

    class Meta():
        db_table = 'product_relations'

class Character(models.Model):
    name      = models.CharField('character name', max_length=30, unique=True)
    image_url = models.URLField('character image URL', max_length=2000)
    
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
    
class Like(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)

    class Meta():
        db_table = 'likes'
    
    def __str__(self):
        return f'{self.user.email} : {self.product.name}'