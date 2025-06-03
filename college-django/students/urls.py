from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='students-dashboard'),
    path('results/', views.result_list, name='students-results'),
    path('profile/', views.profile, name='students-profile'),
]
