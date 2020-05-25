from django.shortcuts import render

from .models import Teacher

def index(request):
  return render(request, 'teachers/teachers.html')