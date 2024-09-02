from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from .views import *

urlpatterns = [
  path('', index),
  path('student/<int:id>', student, name="student_detail")
]