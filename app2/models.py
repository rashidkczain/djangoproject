from django.db import models

# Create your models here.
class Signup(models.Model):
    Name=models.CharField(max_length=20,default='')
    Age=models.IntegerField(default='')
    Email=models.EmailField(default='')
    Password=models.CharField(max_length=8,default='')

class Gallery(models.Model):
    Photo=models.ImageField(upload_to="media/",null=True,blank=True,default='')
    Name=models.CharField(max_length=20)
    Model=models.CharField(max_length=20)
    Price=models.IntegerField()
    
