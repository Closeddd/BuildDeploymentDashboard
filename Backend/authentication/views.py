import bcrypt
from django.contrib.auth import login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.http import HttpResponseRedirect


# Register view
def register(request):
    if request.method == 'POST':
        # Get user data from the form
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']

        # Hash password using bcrypt
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

        # Create user object
        user = User(username=username, password=hashed_password, email=email)
        user.save()

        return HttpResponseRedirect('login/')

    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})


# Login view
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            # Get user by username
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            user = None

        if user is not None and bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
            # If the username and password match, log in the user
            login(request, user)
            return JsonResponse({'status': 'success', 'message': 'Login successful.'})

        else:
            # If authentication fails, return an error message
            return JsonResponse({'status': 'error', 'message': 'Invalid username or password.'})
            # Render the login page with an error message

    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})
