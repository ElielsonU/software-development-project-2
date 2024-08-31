from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import *
from .forms import *

# Create your views here.
def index(req: HttpRequest):
  if req.method == "POST":
    form = StudentForm(req.POST, req.FILES)
    if (form.is_valid()): form.save()
    return redirect("/")
  if req.method == "DELETE":
    id = req.content_params.get("id")
    Student.objects.delete(id)
    return redirect("/")
  students = Student.objects.all()
  form = StudentForm()
  return render(req, 'index.html', { 'students': students, 'form': form })

def student(req: HttpRequest, id):
  student = Student.objects.get(id=id)
  return render(req, 'student.html', { 'student': student }, )