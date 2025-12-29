# team/urls.py
from django.urls import path
from . import views

app_name = 'team'

urlpatterns = [
    path('', views.team, name='team'),
    path('member/<int:pk>/', views.member_detail, name='member_detail'),
]
