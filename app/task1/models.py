from django.db import models


# Create your models here.

class Buyer(models.Model):  # 1.Buyer - модель представляющая покупателя.
    name = models.CharField(max_length=100)  # name - имя покупателя(username аккаунта)
    balance = models.DecimalField(max_digits=10, decimal_places=3)  # balance - баланс(DecimalField)
    age = models.IntegerField()  # age - возраст.


class Game(models.Model):  # 2.Game - модель представляющая игру.
    title = models.CharField(max_length=100)  # title - название игры
    cost = models.DecimalField(max_digits=10, decimal_places=3)  # cost - цена(DecimalField)
    size = models.DecimalField(max_digits=10, decimal_places=3)  # size - размер файлов игры(DecimalField)
    description = models.TextField()  # description - описание(неограниченное кол-во текста)
    age_limited = models.BooleanField(default=False)  # age_limited - ограничение возраста 18+
    buyer = models.ManyToManyField(Buyer, related_name='game')  # buyer - покупатель обладающий игрой
