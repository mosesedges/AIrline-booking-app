from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    return render(request, 'users/users.html')


def login_request(request):
    if request.method == 'POST':
        # Accessing username and password from form data
        username = request.POST['username']
        password = request.POST['password']

        # check if username and password are correct, returning user object if so
        user = authenticate(request, username=username, password=password)

        # if user object is returned, log in and route to index page
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        # otherwise, return login page with  new context
        else:
            return render(request, 'users/login.html', {
                'message': 'Invalid Credentials'
            })
    return render(request, 'users/login.html')


def logout_request(request):
    logout(request)
    return render(request, 'users/login.html', {
        'message': 'Logged Out'
    })
