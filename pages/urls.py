from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('privacypolicy', views.privacy, name='privacy'),
    path('cookiespolicy', views.cookies, name='cookies'),
    path('conditionsofuse', views.conditions, name='conditions'),
]