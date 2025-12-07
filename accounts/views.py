from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import LoginForm
from django.shortcuts import render
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('accounts:dashboard')
    else:
        form = LoginForm(request)
    return render(request, 'accounts/login.html', {'form': form})

@login_required
def dashboard(request):
    return render(request, 'accounts/dashboard.html', {})
@login_required
def home(request):
    return render(request, 'accounts/home.html')