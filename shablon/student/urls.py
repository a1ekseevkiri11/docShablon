from django.urls import path
from . import views


urlpatterns = [
    path('practices/', views.PracticeListView.as_view(), name='student-practice-list'),
    path('practice/<int:pk>/', views.PracticeDetailView.as_view(), name='student-practice-detail'),
    path('practiceStudent/<int:practice_pk>/new/', views.PracticeStudentCreateView.as_view(), name='student-practice-student-new'),
    path('practiceStudent/<int:practice_id>/update/<int:pk>/', views.PracticeStudentUpdateView.as_view(), name='student-practice-student-update'),
]