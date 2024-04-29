from django.shortcuts import render

from django.contrib.auth.mixins import (
    LoginRequiredMixin, 
    UserPassesTestMixin
)

from django.views.generic import ListView
from student.models import DirectionOfTraining

from registration.permission import isSupervisorOPOP


class SupervisorOPOPMixin(LoginRequiredMixin, UserPassesTestMixin):
    
    def test_func(self):
        return isSupervisorOPOP(self.request.user)
    

class DirectionOfTrainingListView(ListView, SupervisorOPOPMixin):
    template_name = 'supervisorOPOP/direction_of_training_list.html'
    context_object_name = 'directions'

    def get_queryset(self):
        return DirectionOfTraining.objects.filter(supervisorOPOP=self.request.user.supervisoropop)

