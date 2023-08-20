from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

# Forms
from .forms import RegisterForm

# Flash Messages
from django.contrib import messages



# Create your views here.
def registerPage(request):

    # Redirect users authenticated back to homepage
    if request.user.is_authenticated:
        return redirect('content:dashboard')

    form = RegisterForm()

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, f'Account registered successfully for {user}')
            
            return redirect('login')

    context = {
        'form': form,
    }

    return render(request, 'users/register.html', context)

def loginPage(request):
    
    # Redirect users authenticated back to homepage
    if request.user.is_authenticated:
        return redirect('content:dashboard')
        
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('content:dashboard')
        else:
            messages.info(request, 'Username OR password is incorrect.')
            # return render(request, 'users/login.html', context)   


    context = {}
    return render(request, 'users/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('users:login')
