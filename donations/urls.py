from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='donations'),
    path('charge', views.charge, name='charge'),
    path('success', views.success, name='success'),
]