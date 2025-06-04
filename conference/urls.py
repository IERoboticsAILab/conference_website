from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('livestream/', views.livestream, name='livestream'),
    path('<int:year>/', views.conference_year, name='conference_year'),
] 