from . import views
from django.urls import path

urlpatterns = [
    path('', views.demo, name='index'),
   # path('index/',views.index,name="index"),
   # path('add/', views.addition, name='result'),
]
