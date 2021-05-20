from django.db import models

class OrderList(models.Model):
     quantity = models.PositiveSmallIntegerField()
     product  = models.ForeignKey('products.Product', on_delete=models.CASCADE)
     order    = models.ForeignKey('Order', on_delete=models.CASCADE)

     class Meta():
         db_table = 'order_lists'

class Order(models.Model):
     reciever_name = models.CharField(max_length=30)
     user          = models.ForeignKey('users.User', on_delete=models.CASCADE)
     order_status  = models.ForeignKey('OrderStatus', on_delete=models.CASCADE)
     updated_at    = models.DateTimeField(auto_now=True)
     class Meta():
         db_table = 'orders'

class OrderStatus(models.Model):
     status = models.BooleanField()

     class Meta():
         db_table = 'order_status'