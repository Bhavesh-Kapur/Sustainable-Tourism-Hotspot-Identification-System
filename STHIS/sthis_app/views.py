from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User,location
import os


# Create your views here.


def register(request):
    return render(request,"register.html")


def home(request):
    return render(request,"home.html")


# views.py


def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            user = User.objects.get(email=email, password=password)
            # If user is found, you can redirect to a dashboard page or any other page
            return redirect('home')
        except User.DoesNotExist:
            if request.method=='POST':
                c = User()
                c.name = request.POST.get('name')
                c.email = request.POST.get('email')
                c.password = request.POST.get('password')
                c.country = request.POST.get('country')

            c.save()
            messages.success(request, f'New User created' ,extra_tags='posted')
            return redirect('home')
            return render(request, 'register.html')

            
    else:
        return render(request, 'register.html')


def admindashboard(request):
    return render(request,'admindashboard.html')

def locationList(request):
    return render(request,'locationList.html')



def destination(request):
    return render(request,'destination.html')


def addLocation(request):
    if request.method=='POST':
        c = location()
        c.name = request.POST.get('name')
        c.desc = request.POST.get('desc')
        c.add = request.POST.get('add')
        c.acti = request.POST.get('acti')
        c.culture = request.POST.get('culture')
        c.save()
        print(c)
        messages.success(request, f'New location added ' ,extra_tags='posted')
        return redirect('addLocation')
    return render(request, 'addLocation.html')
    

# def dashboard(request):
#     # Logic for rendering the dashboard page
#     return render(request, 'dashboard.html')


# from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login, logout
# from .forms import RegistrationForm  # Import custom registration form

# def register(request):
#     if request.method == 'POST':
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)  # Log in the newly registered user
#             return redirect('home')  # Redirect to your desired page after registration
#     else:
#         form = RegistrationForm()

#     context = {'form': form}
#     return render(request, 'register.html', context)



# def register(request):
#     if request.method == 'POST':
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             # Save the user data to the database
#             user = form.save()
#             user.refresh_from_db()
#             user.profile.full_name = form.cleaned_data.get('Name')
#             user.profile.country = form.cleaned_data.get('country')
#             user.save()

#             # # Log the user in
#             # username = form.cleaned_data.get('email')
#             # raw_password = form.cleaned_data.get('password')
#             # user = authenticate(username=username, password=raw_password)
#             # login(request, user)
#             # Redirect to the login page
#             messages.success(request, 'Registration successful! You can now log in.')
#             return redirect('home')
#             pass
#     else:
#         form = RegistrationForm()

#     return render(request, 'register.html', {'form': form})


# def register(request):
#     if request.method == 'POST':
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             # Save the user data to the database
#             user = User.objects.create_user(
#                 username=form.cleaned_data.get('email'),
#                 password=form.cleaned_data.get('password'),
#                 first_name=form.cleaned_data.get('Name'),
#             )

#             profile = Profile.objects.create(user=user)
#             profile.country = form.cleaned_data.get('country')
#             profile.save()

#             # Log the user in
#             username = form.cleaned_data.get('email')
#             raw_password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)

#             # Redirect to the login page
#             messages.success(request, 'Registration successful! You can now log in.')
#             return redirect('home')
#     else:
#         # form = RegistrationForm()
#         return render(request, 'register.html')

#     return render(request, 'register.html', {'form': form})



# def sign_in(request):
#     if request.method == 'POST':
#         email = request.POST['email']
#         password = request.POST['password']

#         # Authenticate the user
#         person = authenticate(email=email, password=password)
#         if person is not None:
#             # Log the user in
#             login(request, person)

#             # Redirect to the home page
#             messages.success(request, 'Sign-in successful!')
#             return redirect('home')
#         else:
#             # Display an error message
#             messages.error(request, 'Invalid email or password')
#     else:
#         # Display the sign-in form
#         form = PersonForm()

#     return render(request, 'registration/sign_in.html', {'form': form})





# def register(request):
#     if request.method == 'POST':
#         form = Person(request.POST)
#         if form.is_valid():
#             # Save the user data to the database
#             form.save()

#             # Log the user in
#             email = form.cleaned_data.get('email')
#             password = form.cleaned_data.get('password')
#             person = authenticate(email=email, password=password)
#             login(request, person)

#             # Redirect to the home page
#             messages.success(request, 'Registration successful! You can now log in.')
#             return redirect('home')
#     else:
#         form = PersonForm()

#     return render(request, 'registration/register.html', {'form': form})