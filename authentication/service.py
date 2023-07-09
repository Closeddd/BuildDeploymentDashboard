from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.utils import json
import bcrypt


def register(data):
    try:
        username = data['username']
        password = data['password']
        email = data['email']

        # Hash password using bcrypt
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

        # Check if the username is already taken
        if User.objects.filter(username=username).exists():
            return False, 'Username already taken'

        # Create a new user
        user = User(username=username, password=hashed_password, email=email)
        user.save()
        return True, 'User registered successfully'

    except Exception as e:
        return False, str(e)


def register_staff(data):
    try:
        username = data['username']
        password = data['password']
        email = data['email']

        # Hash password using bcrypt
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

        # Check if the username is already taken
        if User.objects.filter(username=username).exists():
            return False, 'Username already taken'

        # Create a new user
        user = User(username=username, password=hashed_password, email=email, is_staff=True)
        user.save()
        return True, 'Employee registered successfully!'

    except Exception as e:
        return False, str(e)


def login_service(request):
    try:
        form = request.data
        username = form['username']
        password = form['password']

        # Get user by username
        user = User.objects.get(username=username)
        if user is not None and bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
            login(request,user)
            return True, 'Logged in successfully!'

    except User.DoesNotExist:
        return False, 'Invalid username'


def logout_service(request):
    try:
        logout(request)
        return True, 'you have logged out! have a nice day!'

    except Exception as e:
        return False, str(e)
