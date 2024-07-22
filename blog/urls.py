from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('carne_list/', views.carne_list, name='carne_list'),
    path('bebida_list/', views.bebida_list, name='bebida_list'),
]
