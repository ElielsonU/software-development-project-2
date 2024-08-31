from django.urls import path
from .views import *

urlpatterns = [
  path('', index),
  path('student/<int:id>', student, name="student_detail")
]