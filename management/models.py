from django.db import models


class Course(models.Model):
  name = models.CharField(max_length=200)
  description = models.TextField()

  def __str__(self):
    return self.name

# Create your models here.
class City(models.Model):
  name = models.CharField(max_length=200)
  cep = models.TextField(max_length=8)

  def __str__(self):
    return self.name

class Student(models.Model):
  name = models.CharField(max_length=200)
  email = models.EmailField()
  cpf = models.CharField(max_length=11)
  birthday = models.DateField()
  image = models.ImageField(upload_to='students/', null=True, blank=True)
  course = models.ForeignKey(Course, on_delete=models.DO_NOTHING, null=True) 
  city = models.ForeignKey(City, on_delete=models.DO_NOTHING, null=True) 

  def __str__(self):
    return self.name