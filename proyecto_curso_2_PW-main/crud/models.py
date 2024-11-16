from django.db import models

# Create your models here.

class BleachCharacter(models.Model):

    name = models.CharField(max_length=300)
    genre = models.CharField(max_length=300)
    height = models.IntegerField()
    weight = models.FloatField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.name



