from django.db import models

# Create your models here.


# 1.Buyer - модель представляющая покупателя.
# Обладает следующими полями:
# name - имя покупателя(username аккаунта)
# balance - баланс(DecimalField)
# age - возраст.

class Buyer(models.Model):
    name = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=6, decimal_places=3)
    age = models.IntegerField()


# 2.Game - модель представляющая игру.

# title - название игры
# cost - цена(DecimalField)
# size - размер файлов игры(DecimalField)
# description - описание(неограниченное кол-во текста)
# age_limited - ограничение возраста 18+ (BooleanField, по умолчанию False)
# buyer - покупатель обладающий игрой (ManyToManyField). У каждого покупателя может быть игра и
# у каждой игры может быть несколько обладателей.


class Game(models.Model):
    title = models.CharField(max_length = 100)
    cost = models.DecimalField(max_digits=6, decimal_places=3)
    size = models.DecimalField(max_digits=6, decimal_places=3)
    models.DecimalField(max_digits=6, decimal_places=3)
    description = models.TextField()
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer, related_name='game')
