from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='organisations'),
    path('<int:organisation_id>', views.organisation, name='organisation'),
]