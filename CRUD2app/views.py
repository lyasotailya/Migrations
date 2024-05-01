from django.views.generic import ListView
from django.shortcuts import render

from .models import Student


def students_list(request):
    template = 'templates/students_list.html'
    ordering = 'group'
    students = Student.objects.order_by(ordering).all()
    context = {'student': students}
    return render(request, template, context)
