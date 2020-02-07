from django.db import models

from django.conf import settings



class customer(models.Model):
    first_name = models.CharField(max_length=20)
    second_name= models.CharField(max_length=20)
    number = models.CharField(max_length=20)
    location = models.CharField(max_length=20)

    def __str__(self):
        return self.first_name

    