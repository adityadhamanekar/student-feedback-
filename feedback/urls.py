from django.urls import path
from . import views

urlpatterns = [
    path('', views.feedback_view, name='feedback'),
    path('success/', views.feedback_success_view, name='feedback_success'),
    path('all_feedback/', views.view_all_feedback, name='all_feedback'),
]
