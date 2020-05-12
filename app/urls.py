from django.urls import path
from app import views

urlpatterns = [
    path('', views.index, name='homepage'),
    path('history/', views.history_view)
]
