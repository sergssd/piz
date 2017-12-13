from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class PizzaShop(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name='pizzashop')
    name = models.CharField(max_length=100, verbose_name='Торговая марка')
    phone = models.CharField(max_length=100, verbose_name=' Телефон')
    address = models.CharField(max_length=100, verbose_name='Адрес')
    logo = models.ImageField(upload_to='pizzashop_logo/', blank=False, verbose_name='Логотип')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name ='Пиццерия'
        verbose_name_plural = 'Пиццерии'


class Pizza(models.Model):
    pizzashop = models.ForeignKey(PizzaShop)
    name = models.CharField(max_length=30, verbose_name='Наименование пиццы')
    short_description = models.CharField(max_length=100, verbose_name='Краткое описание')
    image = models.ImageField(upload_to='pizza_images/', blank=False, verbose_name='Фото пиццы')
    price = models.IntegerField(default=0, verbose_name='Цена за 1шт.')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name ='Пицца'
        verbose_name_plural ='Пиццы'

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='client')
    avatar = models.CharField(max_length=500, verbose_name='Аватарка')
    phone = models.CharField(max_length=20, blank=True, verbose_name='Телефон')
    address = models.CharField(max_length=30, blank=True, verbose_name='Адрес')

    def __str__(self):
        return self.user.get_full_name()
    class Meta:
        verbose_name ='Клиент'
        verbose_name_plural = 'Клиенты'
