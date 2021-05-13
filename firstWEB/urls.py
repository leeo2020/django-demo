from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('calc/', views.calc),
    path('rst/', views.rst)
]
