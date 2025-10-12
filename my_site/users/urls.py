from . import views
from django.urls import path

app_name='users'

urlpatterns = [
    path('login/', views.custom_login, name='custom_login'),
    path('register/', views.register, name='register')
]