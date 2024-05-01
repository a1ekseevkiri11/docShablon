from django.urls import path
from . import views


urlpatterns = [
    path('practiceStudent/', views.PracticeStudentListView.as_view(), name='supervisor-practice-practice-student-list'),
]