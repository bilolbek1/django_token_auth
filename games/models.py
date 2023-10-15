from django.db import models

# Create your models here.

class Games(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    about = models.TextField()


    def __str__(self):
        return self.name