from pickle import TRUE
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Result(models.Model):
    pregnancies = models.CharField(verbose_name="Pregnancies",max_length=2)
    glucose = models.CharField(verbose_name="Glucose", max_length=3)
    blood_pressure = models.CharField(verbose_name="Blood Pressure", max_length=3)
    insulin = models.CharField(verbose_name="Insulin", max_length=3)
    skin_thickness = models.CharField(verbose_name="Skin Thickness", max_length=2)
    bmi = models.FloatField(verbose_name="BMI", max_length=4)
    diabetes_pedigree_function = models.FloatField(verbose_name="Diabetes Pedigree Function", max_length=5)
    age = models.CharField(verbose_name="Age", max_length=3)
    owner = models.ForeignKey(User,on_delete=models.CASCADE,null=TRUE)

class Contact(models.Model):
    name = models.CharField(max_length=50)
    mail = models.EmailField()
    phone = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name

class Ans(models.Model):
    ans = models.CharField(max_length=10)
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.user.username



