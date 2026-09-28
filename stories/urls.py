from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('generate/', views.generate_story_view, name='generate_story'),
    path('stories/<int:pk>/', views.story_detail, name='story_detail'),
    path('stories/<int:pk>/regenerate/', views.regenerate_story, name='regenerate_story'),
    path('stories/<int:pk>/delete/', views.story_delete, name='story_delete'),
    path('history/', views.story_history, name='story_history'),
    path('about/', views.about, name='about'),
]
