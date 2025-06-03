from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='faculty-dashboard'),
    path('courses/', views.course_list, name='faculty-courses'),
    path('profile/', views.profile, name='faculty-profile'),
]
