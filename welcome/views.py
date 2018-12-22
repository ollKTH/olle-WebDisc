from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    title_text = "Hello and welcome!"
    return render(request, 'welcome/welcome.html', {'title_text': title_text})
