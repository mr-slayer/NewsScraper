from django.db import models
# from django import forms
# Create your models here.
class users(models.Model):
    # CHOICES=(
    #     ('sports','Sports'),
    #     ('entertainment','Entertainment'),
    #     ('business','Business'),
    #     ('politics','Politics'),
    #     ('read','Read'),
    # )
    name = models.CharField(max_length = 50,null=True,default=True) 
    
    email = models.EmailField(max_length = 50,null=True,default=True,unique=True) 
    
    password = models.CharField(max_length = 50,null=True,default=True) 
    category=models.CharField(max_length=50,null=True,default=True)
    