from django.urls import path
from . import views

app_name = 'main'  # This line is essential for namespaced URL lookups

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
