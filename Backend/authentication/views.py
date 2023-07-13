import bcrypt
import json
from django.contrib.auth import login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication


# Register view
def register(request):
    try:
        if request.method == 'POST':
            # Get user data from the form
            form = json.loads(request.body)
            username = form['username']
            password = form['password']
            email = form['email']

            # Hash password using bcrypt
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

            # Create user object
            user = User(username=username, password=hashed_password, email=email)
            user.save()

            # return HttpResponseRedirect('login/')
            return JsonResponse({'status': 'Success', 'message': 'test'})
    except Exception as e:
        print(e)
        return JsonResponse({'status': 'Failed', 'message': 'Error'})


    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})


# Login view
def login_view(request):
    if request.method == 'POST':
        input = json.loads(request.body)
        username = input['username']
        password = input['password']

        try:
            # Get user by username
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            user = None

        if user is not None and bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
            # If the username and password match, log in the user
            login(request, user)
            refresh = RefreshToken.for_user(user)
            return JsonResponse(
                {'status': 'success', 'message': 'Login successful.', 'access_token': str(refresh.access_token),
                 'refresh_token': str(refresh)})

        else:
            # If authentication fails, return an error message
            return JsonResponse({'status': 'error', 'message': 'Invalid username or password.'}, status=401)
            # Render the login page with an error message

    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})


def home(request):
    context = {
        'message': 'Welcome to my website!'
    }
    return redirect('home')


def logout_view(request):
    # Remove JWT from the user's browser cookies
    response = JsonResponse({'status': 'success', 'message': 'Logged out successfully'})
    response.delete_cookie('access_token')
    response.delete_cookie('refresh_token')

    # Logout the user from the Django session
    logout(request)

    # Redirect the user to the login page
    return response
