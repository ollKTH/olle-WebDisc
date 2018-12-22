from django.shortcuts import render
from .models import Course

def index(request):
    courses = Course.objects.all()
    return render(request, 'courses/index.html', {'courses': courses})

def detail(request, id):
    print(id)
    course = Course.objects.get(id=id)
    return render(request, 'courses/details.html', {'course': course})
