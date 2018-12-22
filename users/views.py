from django.shortcuts import render
from .models import Profile

def index(request):
    # Get all users and print them
    users = Profile.objects.all()
    return render(request, 'users/index.html', {'users': users})

def detail(request, user_id):
    # Show user details, name + scorecards
    raise NotImplementedError