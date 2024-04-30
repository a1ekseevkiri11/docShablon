from django.urls import path
from . import views


urlpatterns = [
    path('practices/', views.PracticesListView.as_view(), name='practice-list'),
    path('directionOfTraining/<int:pk>/', views.DirectionOfTrainingDetailView.as_view(), name='direction_of_training_detail'),
]