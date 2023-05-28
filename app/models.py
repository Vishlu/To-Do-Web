from django.db import models, reset_queries

# Create your models here.
class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=70)
    password = models.CharField(max_length=100)

   