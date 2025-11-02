from django.shortcuts import render, redirect
from .forms import RegistrationForm, Avtorizations
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.models import User, Group


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            group = Group.objects.get(name='Обычные пользователи')
            user.group.add(group)
            login(request, user)
            return redirect('choice')
    else:
        form = RegistrationForm()
    return render(request, 'users/register.html', {'form': form})


def custom_login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('choice')
        else:
            messages.error(request, 'Неверный логин или пароль')

    return render(request, 'users/login.html',)
