# gallery/urls.py
from django.urls import path
from . import views

app_name = 'gallery'

urlpatterns = [
    path('', views.gallery, name='gallery'),
    path('category/<str:category>/', views.gallery_by_category, name='category'),
]


