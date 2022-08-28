import email
from unicodedata import name
from django.db import models

# Create your models here.
class Student(models.Model):
    sid=models.CharField(max_length=200,primary_key=True)
    name=models.CharField(max_length=100)
    email=models.EmailField()
    phoneno=models.IntegerField()
