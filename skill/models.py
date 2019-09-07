from django.db import models
from django.urls import reverse
from django.conf import settings    # 決済処理用

class Category(models.Model):       # Categoryモデルの定義
    name = models.CharField(max_length=50)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Service(models.Model):       # Serviceモデルの定義
    content = models.CharField(max_length=255)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    price = models.IntegerField(default=10)
    image = models.ImageField(upload_to='photo', null=True)    # 画像カラム追加
    # CategoryモデルとShopモデルの関連付け
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return self.content
    def get_absolute_url(self):
        return reverse('skill:detail', kwargs={'pk': self.pk})

class BuyingHistory(models.Model):
    """購入履歴"""
    service = models.ForeignKey(Service, verbose_name='Purchase Service', on_delete=models.PROTECT)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Purchase User', on_delete=models.PROTECT)
    is_sended = models.BooleanField('Shipping flag', default=False)
    stripe_id = models.CharField('Purchase_id', max_length=200)
    created_at = models.DateTimeField('Date', auto_now_add=True)

    def __str__(self):
        return '{} {} {}'.format(self.service, self.user.email, self.is_sended)

def get_absolute_url(self):
    # reverse関数を使用して、viewの名前からリダイレクト先を取得
    return reverse('skill:detail', kwargs={'pk': self.pk})
