from django.db import models

# Create your models here.
class Doctor(models.Model):
	name=models.CharField(max_length=50)
	mobile=models.IntegerField()
	special=models.CharField(max_length=50)

	def __str__(self):
		ret = self.name+','+self.special
		return ret

class Patient(models.Model):
	name=models.CharField(max_length=50)
	gender=models.CharField(max_length=50)
	mobile=models.IntegerField(null=True)
	address=models.CharField(max_length=150)

	def __str__(self):
		re = self.name
		return re

	

class CardiologistDepartment(models.Model):
	doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
	patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
	date1=models.DateField()
	time1=models.TimeField()

	def __str__(self):
		r = self.doctor+','+self.patient
		return r



	

class NeurologistDepartment(models.Model):
	doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
	patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
	date1=models.DateField()
	time1=models.TimeField()

	def __str__(self):
		r = self.doctor+','+self.patient
		return r

class SurgeonDepartment(models.Model):
	doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
	patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
	date1=models.DateField()
	time1=models.TimeField()

	def __str__(self):
		r = self.doctor+','+self.patient
		return r