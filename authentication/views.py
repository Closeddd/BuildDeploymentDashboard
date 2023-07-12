from django.shortcuts import redirect
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from authentication import service


# Register view
@api_view(['POST'])
def register(request):
    success, message = service.register(request.data)
    if success:
        return Response({'message': message}, status=status.HTTP_201_CREATED)
    else:
        return Response({'error': message}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAdminUser])  # automatically checked if logged in and is_staff == 1
def register_staff(request):
    success, message = service.register_staff(request.data)
    if success:
        return Response({'message': message}, status=status.HTTP_201_CREATED)
    else:
        return Response({'error': message}, status=status.HTTP_400_BAD_REQUEST)


# Login view
@api_view(['POST'])
def login_view(request):
    success, message = service.login_service(request)
    if success:
        return Response({'message': message}, status=status.HTTP_201_CREATED)
    else:
        return Response({'error': message}, status=status.HTTP_400_BAD_REQUEST)


@api_view()
@permission_classes([IsAuthenticated])
def home(request):
    context = {
        'message': 'Welcome to my website!'
    }
    return redirect('home')


@api_view()
@permission_classes([IsAuthenticated])
def logout_view(request):
    success, message = service.logout_service(request)
    if success:
        return Response({'message': message}, status=status.HTTP_201_CREATED)
    else:
        return Response({'error': message}, status=status.HTTP_400_BAD_REQUEST)