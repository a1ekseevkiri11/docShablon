from django.shortcuts import render

from django.contrib.auth.mixins import (
    LoginRequiredMixin, 
    UserPassesTestMixin
)

from django.views.generic import (
    ListView,
    DetailView,
    View
)

from user.models import (
    DirectionOfTraining,
    Group,
    Practice,
)

from registration.permission import isSupervisorOPOP


class SupervisorOPOPMixin(LoginRequiredMixin, UserPassesTestMixin):
    
    def test_func(self):
        return isSupervisorOPOP(self.request.user)
    

#TODO сделать фильтры и поиск
class PracticesListView(ListView, SupervisorOPOPMixin):
    template_name = 'supervisorOPOP/practice_list.html'
    context_object_name = 'practices'

    def get_queryset(self):
        return Practice.objects.filter(supervisorOPOP=self.request.user.supervisoropop)
    



class DirectionOfTrainingDetailView(DetailView, SupervisorOPOPMixin):
    model = DirectionOfTraining
    template_name = 'supervisorOPOP/direction_of_training_detail.html'
    context_object_name = 'direction'
