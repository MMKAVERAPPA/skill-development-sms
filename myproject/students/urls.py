from django.urls import path
from . import views


urlpatterns = [
    path('', views.student, name='student'),
    path('profile/', views.profile, name='profile'),
    path('home/', views.home, name='home'),
    path('contact/', views.contact,name='contact'),
]
