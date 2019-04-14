from django.urls import path
from.import views

urlpatterns = [
    path('organization/', views.organization, name='Organization'),
]