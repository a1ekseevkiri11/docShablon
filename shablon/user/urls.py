from django.urls import path
from . import views


urlpatterns = [
    path('report/', views.GenerateReportView.as_view(), name='report'),
]