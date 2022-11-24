from django.urls import path 
from . import views

urlpatterns = [
    path('detail/', views.detail_pays_view, name='detail'),
]