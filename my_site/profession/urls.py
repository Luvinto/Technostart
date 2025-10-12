from . import views
from django.urls import path

urlpatterns=[
    path('', views.vibor ,name='choice'),
    path('profession_index/', views.profession_index, name='profession_index'),
    path('presintations_list/', views.presintations_list, name='presintations_list'),
    path('download/<int:pk>/', views.download_presentation, name='download_presentation'),
    path('engineering_processes_index/', views.engineering_processes_index, name='engineering_processes_index'),
    path('post_professions/<slug:post_slug>', views.show_post, name='post_professions'),
    path('post_engineering/<slug:post_slug>', views.engineering_processes, name='post_engineering')

]