from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import InstitutionRegisterForm


def register(request):
    if request.method == 'POST':
        form = InstitutionRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You can now Login {username}!')
            return redirect('login')
    else:
        form = InstitutionRegisterForm()
    return render(request, 'institutions/register.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'institutions/profile.html')