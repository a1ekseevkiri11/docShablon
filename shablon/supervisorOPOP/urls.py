from django.urls import path
from . import views


urlpatterns = [
    path('directionOfTraining/', views.DirectionOfTrainingListView.as_view(), name='direction_of_training_list'),
]