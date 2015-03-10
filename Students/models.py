from django.db import models

# Create your models here.


class Student(models.Model):
	idnum = models.CharField(max_length=8)
	name = models.CharField(max_length=100)
	fathername = models.CharField(max_length=100)
	gender = models.CharField(max_length=10)
	dob = models.CharField(max_length=100)
	addr = models.TextField()
	mobile = models.CharField(max_length=12)
	email = models.EmailField(max_length=200)
	def __str__(self):
		return self.idnum+":"+self.name