from django.db import models

# Create your models here.
class Goods(models.Model):  # 商品
    name = models.CharField(max_length=32,verbose_name="名称")
    price = models.FloatField(verbose_name="价格")


class Order(models.Model):  # 订单
    no = models.CharField(max_length=64,verbose_name="订单号")
    goods = models.ForeignKey(to='Goods',on_delete=models.CASCADE,verbose_name="商品ID")
    a = models.ManyToManyField
    status_choices = (
        (1,'未支付'),
        (2,'已支付'),
    )
    status = models.SmallIntegerField(choices=status_choices,default=1,verbose_name="支付状态")