from django.urls import path
from . import views


urlpatterns = [
    path('practiceStudent/', views.PracticeStudentListView.as_view(), name='supervisor-practice-practice-student-list'),
    path('practiceStudent/<int:pk>/', views.PracticeStudentDetailView.as_view(), name='supervisor-practice-practice-student-detail'),
    path('practiceStudent/update/<int:pk>/', views.PracticeStudentUpdateView.as_view(), name='supervisor-practice-practice-student-update'),
]