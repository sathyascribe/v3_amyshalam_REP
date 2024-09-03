from .forms import LoginForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required





def login_page(request):
    form = LoginForm()
    message = ''

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('accounts:index')
            else:
                message = 'Login failed!'
    return render(request, 'login.html', context={'form': form, 'message': message})

@login_required()
def dashboard(request):
    return render(request, 'dashboard.html')


def logout_user(request):
    logout(request)
    return redirect('accounts:login')
