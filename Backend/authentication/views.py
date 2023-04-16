from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import login
import bcrypt

# Create your views here.

def register(request):
    if request.method == 'POST':
        
        #get user data from the form 
        username = request.POST['username']
        password = request.POST['password']        
        email = request.POST['email']
        role = request.POST['role']
        
        #hashing password that is being used for registration
        password = password.encode('utf-8')
        salt = bcrypt.gensalt()
        hashed_password =bcrypt.hashpw(password,salt)
        
        #Creating instance of User(django) object

        user = User.objects.create_user(username=username, password=hashed_password, email=email,role=role)
        user.save() # based on the metadata given django automatically stores the data to right table in schema

        login(request.user)
        
        return redirect('home')
    
    return render(request,'register.html') #not sure how react would call the API
         
def login(request):
    pass