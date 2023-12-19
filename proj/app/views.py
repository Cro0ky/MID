from django.shortcuts import render
from .models import *


def index(request):
    # company = Company.objects.get(name='Metro')
    # products = company.products_set.all()
    # tom = Students.objects.create(name='Tom')
    # students = tom.course.create(name='Algebra')
    courses = Students.objects.get(name='Student 1').course.all()
    student = Students.objects.filter(course__name='1')
    return render(request, 'app/index.html', context={"student": student})
