from django.shortcuts import render
from django.http import HttpRequest
from .models import *

# Create your views here.
def index(req: HttpRequest):
  students = Student.objects.all()
  return render(req, 'index.html', { 'students': students })