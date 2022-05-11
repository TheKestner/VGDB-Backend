from django.urls import path
from . import views

urlpatterns = [
    path('vgdb/', views.vgdb_all),
    path('', views.index, name='index'),
]