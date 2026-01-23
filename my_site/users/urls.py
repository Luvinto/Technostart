from . import views
from django.urls import path


urlpatterns = [
    path('login/', views.custom_login, name='custom_login'),
    path('register/', views.register, name='register'),
    path('download-consent/', views.download_consent_agreement, name='download_consent_agreement'),
]