from django.urls import path
from . import views

urlpatterns = [
    path('', views.reclamos_list, name='reclamos_list'),
    path('reclamo/<int:pk>/', views.reclamo_detail, name='reclamo_detail'),
    path('reclamo/new/', views.reclamo_new, name='reclamo_new'),
    path('reclamo/<int:pk>/edit/', views.reclamo_edit, name='reclamo_edit'),
]