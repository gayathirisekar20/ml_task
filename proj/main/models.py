from django.db import models

# Create your models here.

class Cereal(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    mrf=models.CharField(max_length=10)
    type=models.CharField(max_length=10)
    calories=models.FloatField(default=0)
    protein=models.FloatField(default=0)
    fat=models.IntegerField(default=0)
    sodium=models.IntegerField(default=0)
    fiber=models.FloatField(default=0)
    carbo=models.FloatField(default=0)
    sugars=models.IntegerField(default=0)
    potass=models.IntegerField(default=0)
    vitamins=models.IntegerField(default=0)
    shelf=models.IntegerField(default=0)
    weight=models.FloatField(default=0)
    cups=models.FloatField(default=0)
    rating=models.FloatField(default=0)
    procal=models.IntegerField(default=0)

    def __str__(self):
        return self.name
