from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('profile/', views.profile, name='profile'),
    path('home/', views.home, name='home'),
    path('update/<int:id>', views.student_update, name='student_update'),
    path('update/<int:id>', views.student_update, name='student_update'),
    path('contact/', views.contact, name='contact'),
    path('create/', views.student_create, name='student_create'),
]
