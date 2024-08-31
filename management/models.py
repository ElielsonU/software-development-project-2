from django.db import models

# Create your models here.
class Student(models.Model):
  name = models.CharField(max_length=200)
  email = models.EmailField()
  cpf = models.CharField(max_length=11)
  birthday = models.DateField()
  image = models.ImageField(upload_to='students/', null=True, blank=True)