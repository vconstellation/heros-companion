from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='layout-home'),
    path('journal/', views.journal, name='layout-journal'),
]