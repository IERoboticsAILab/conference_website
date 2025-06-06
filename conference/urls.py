from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('livestream/', views.livestream, name='livestream'),
    path('markdown-demo/', views.markdown_demo, name='markdown_demo'),
    path('<int:year>/', views.conference_year, name='conference_year'),
] 