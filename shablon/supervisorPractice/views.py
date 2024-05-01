from django.shortcuts import render

from django.contrib.auth.mixins import (
    LoginRequiredMixin, 
    UserPassesTestMixin
)

from django.views.generic import (
    ListView,
    DetailView,
    View,
    CreateView,
    UpdateView,
    DeleteView,
    ListView
)


from registration.permission import isSupervisorPractice

from user.models import (
    PracticeStudent
)


class SupervisorPracticeMixin(LoginRequiredMixin, UserPassesTestMixin):
    
    def test_func(self):
        return isSupervisorPractice(self.request.user)




class PracticeStudentListView(ListView, SupervisorPracticeMixin):
    template_name = 'supervisorPractice/practice_student_list.html'
    context_object_name = 'practices'

    model = PracticeStudent



class PracticeDetailView(View, SupervisorPracticeMixin):
    # + выводить отчет если он уже есть, его можно будет только создать 
    # и редактировать
    pass


class PracticeStudentCreateView(CreateView, SupervisorPracticeMixin):
    pass


class PracticeStudentUpdateView(UpdateView, SupervisorPracticeMixin):
    pass