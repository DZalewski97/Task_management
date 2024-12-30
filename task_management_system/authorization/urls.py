from django.urls import path
from . import views

urlpatterns = [
    path('', views.people_list, name='people_list'),
    path('<int:pk>/', views.find_id, name='find_id'),
    path('add/', views.add_new_people, name='add_new_people'),
    path('delete/<int:pk>/', views.delete_people, name='delete_people'),
    path('registration/', views.registration , name='registration'),
    path('registration/submit', views.registration_confirm , name='registration_confirm'),
    path('login/', views.login, name='login'),
    path('login/check', views.login_check, name='login_check'),
]
