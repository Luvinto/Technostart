
from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegistrationForm, Avtorizations
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.models import User, Group
from django.http import HttpResponse, Http404, FileResponse
import os
from django.conf import settings


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            next_url = request.POST.get('next') or request.GET.get('next')
            if next_url:
                return redirect(next_url)
            else:
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
            next_url = request.POST.get('next') or request.GET.get('next')
            if next_url:
                return redirect(next_url)
            else:
                return redirect('choice')
        else:
            messages.error(request, 'Неверный логин или пароль')

    return render(request, 'users/login.html')

def download_consent_agreement(request):
    file_path=os.path.join(settings.MEDIA_ROOT, 'agreements', 'Согласие на обработку персональных данных.docx')
    if not os.path.exists(file_path):
        raise Http404("Файл согласия не найден")
    response=FileResponse(
        open(file_path,'rb'),
        content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document',
        as_attachment=True,
        filename='Согласие на обработку персональных данных.docx'
    )
    return response