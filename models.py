from django.db import models

# Create your models here.
class search_posts(models.Model):
  
    name = models.CharField(max_length = 30)
    plus = models.CharField(max_length = 2)
    upload = models.CharField(max_length =2)
    staffpick = models.CharField(max_length =2)
    url = models.CharField(max_length = 80)
    