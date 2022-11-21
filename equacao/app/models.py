from django.db import models

class User(models.Model):
  a = models.IntegerField('a')
  b = models.IntegerField('b')
  c = models.IntegerField('c')
  raiz1 = 0
  raiz2 = 0

  def __str__(self):
    return f"a: {self.a}, b: {self.b}, c: {self.c}"
