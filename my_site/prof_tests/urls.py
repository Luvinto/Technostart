from . import views
from django.urls import path

urlpatterns=[
    path('',views.prof_test, name='prof_test')
]