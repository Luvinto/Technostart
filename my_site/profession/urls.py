from . import views
from django.urls import path

urlpatterns=[
    path('', views.vibor ,name='choice'),
    path('presintations_list/', views.presintations_list, name='presintations_list'),
    path('download_presentation_file/<int:pk>/', views.download_presentation_file, name='download_presentation_file'),
    path('download_presentation_file_met/<int:pk>/', views.download_presentation_file_met, name='download_presentation_file_met'),
    path('engineering_processes_index/', views.engineering_processes_index, name='engineering_processes_index'),
    path('post_professions/<slug:post_slug>', views.show_post, name='post_professions'),
    path('post_engineering/<slug:post_slug>', views.engineering_processes, name='post_engineering')
]