from django.db import models

# Create your models here.


class register(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.Charfield(max_lenght=30)
    email = models.Charfield(max_lenght=30)
    password1 = models.Charfield(max_lenght=30)
    password2 = models.Charfield(max_lenght=30)
    

    