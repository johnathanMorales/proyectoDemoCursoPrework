from django.shortcuts import render

from django.http import HttpResponse
from .models import Student
# Create your views here.
def index(request):
    estudiantes = Student.objects.all()
    context = {'clase': 'Aprendiendo Django', 'estudiantes': estudiantes}
    return render(request, 'student_list.html', context)
