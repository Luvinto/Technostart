
from django.shortcuts import render

# Create your views here.

def index(req):

    return render(req,'main/index.html')

def about(req):

    return render(req, 'main/about.html')

from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponseForbidden
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.views import redirect_to_login
from django.conf import settings
from django.shortcuts import redirect
from django.urls import reverse # Импортируем reverse

def custom_admin(request):
    if not request.user.is_authenticated:
        full_path=request.get_full_path()
        set_views=settings.LOGIN_URL
        return redirect_to_login(full_path, set_views, REDIRECT_FIELD_NAME)
    if not request.user.is_staff:
        return HttpResponseForbidden("Ошибка 403 Доступ запрещен: У вас нет прав доступа к странице администратора.")

    return redirect('admin:index')


