import bcrypt
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import redirect
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.utils import json


# Register view
@api_view(['POST'])
def register(request):

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

    return JsonResponse({'status': 'success', 'message': 'You have successfully registered!'})


@api_view(['POST'])
@permission_classes([IsAdminUser])  # automatically checked if logged in and is_staff == 1
def register_staff(request):
    form = request.data
    username = form['username']
    password = form['password']
    email = form['email']

    # Hash password using bcrypt
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    # Create user object
    user = User(username=username, password=hashed_password, email=email, is_staff=True)
    user.save()

    return JsonResponse({'status': 'success', 'message': 'You have successfully registered an employee!'})


# Login view
@api_view(['POST'])
def login_view(request):
    form = request.data
    username = form['username']
    password = form['password']

    try:
        # Get user by username
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        user = None

    if user is not None and bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
        # If the username and password match, log in the user
        login(request, user)
        # refresh = RefreshToken.for_user(user)
        # return JsonResponse(
        #     {'status': 'success', 'message': 'Login successful.', 'access_token': str(refresh.access_token),
        #      'refresh_token': str(refresh)})

    else:
        # If authentication fails, return an error message
        return JsonResponse({'status': 'error', 'message': 'Invalid username or password'}, status=401)
        # Render the login page with an error message

    return JsonResponse({'message': 'you have logged in!'})


@api_view()
def home(request):
    context = {
        'message': 'Welcome to my website!'
    }
    return redirect('home')


@api_view()
def logout_view(request):
    # Remove JWT from the user's browser cookies
    response = JsonResponse({'status': 'success', 'message': 'Logged out successfully'})

    # Logout the user from the Django session
    logout(request)

    # Redirect the user to the login page
    return response
