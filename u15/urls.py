from django.urls import path
from.import views

urlpatterns = [
    path('', views.home, name='u15-home'),
    path('about/', views.about, name='u15-about'),
]