from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Scholarship(models.Model):
	image=models.ImageField(upload_to='Uploads/products/', blank=True)
	sponsor =models.CharField(max_length=100)
	details=models.TextField(max_length=2000,blank=True)
	summary=models.TextField(max_length=1000, blank=True)
	start =models.DateTimeField()
	expire =models.DateTimeField()
	def __str__(self):
		return self.sponsor

class Form1(models.Model):
	name =models.CharField(max_length=100)
	email= models.EmailField()
	age=models.CharField(max_length=100)
	date_of_birth =models.DateTimeField()
	nationality=models.CharField(max_length=100)
	def __str__(self):
		return self.name
class Income(models.Model):
	name =models.CharField(max_length=100)
	def __str__(self):
		return self.name
class Level(models.Model):
	name =models.CharField(max_length=100)
	def __str__(self):
		return self.name

class Form2(models.Model):
	Cv =models.FileField(blank=True,null=True)
	last_level_of_studying=models.ForeignKey(Level,
                                on_delete=models.CASCADE)
	letter_to_employer=models.TextField(max_length=1000)
	def __str__(self):
		return self.name

	
