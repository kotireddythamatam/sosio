from django.db import models

# Create your models here.
class Sosio_model(models.Model):
    wish = models.CharField(max_length=254)
    date = models.DateField()
    
