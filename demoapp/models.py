from django.db import models

# Create your models here.

class Widget(models.Model):
    name = models.CharField(max_length=140)
    font_size=models.IntegerField()
    
class MyUser(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    city = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.first_name}"

        