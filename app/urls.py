from django.urls import path
from . import views

urlpatterns = [
    path ('', views.index, name='index'),
    path ('edit/<id>', views.edit, name='edit'),
    path ('delete/<id>', views.delete, name='delete'),

]