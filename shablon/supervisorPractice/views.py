from django.shortcuts import render, get_object_or_404

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

from django.db.models import Q


from registration.permission import isSupervisorPractice

from user.models import (
    PracticeStudent,
    Practice
)

from .forms import (
    PracticeStudentFormSupervisorPractice,
)

from .filters import (
    PracticeStudentFilter,
)

from .queryset import (
    get_queryset_practice_student_for_SupervisorPractice,
)

from django.urls import (
    reverse_lazy,
    reverse,
)


class SupervisorPracticeMixin(LoginRequiredMixin, UserPassesTestMixin):

    def extra_test_func(self):
        return True
    
    def test_func(self):
        return isSupervisorPractice(self.request.user) and self.extra_test_func()




class PracticeStudentListView(ListView, SupervisorPracticeMixin):
    template_name = 'supervisorPractice/practice_student_list.html'
    context_object_name = 'practices'


    def get_queryset(self):
        queryset = get_queryset_practice_student_for_SupervisorPractice(self.request.user.supervisorpractice)
        query = self.request.GET.get('q')
        filters = self.request.GET
        
        if query:
            queryset = queryset.filter(Q(title__icontains=query))
        
        self.filterset = PracticeStudentFilter(filters, queryset=queryset, supervisorpractice=self.request.user.supervisorpractice,)
        return self.filterset.qs
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filters'] = self.filterset.form
        context['applied_filters'] = self.request.GET.urlencode()
        return context



class PracticeStudentDetailView(View, SupervisorPracticeMixin):
    template_name = 'supervisorPractice/practice_student_detail.html'

    def get(self, request, pk):
        practice_student = get_object_or_404(PracticeStudent, pk=pk)
        context = {}
        context['practice'] = practice_student.practice
        context['practice_student'] = practice_student
        return render(request, self.template_name, context)


class PracticeStudentUpdateView(UpdateView, SupervisorPracticeMixin):
    template_name = 'supervisorPractice/practice_student_form.html'
    model = PracticeStudent
    form_class = PracticeStudentFormSupervisorPractice

    def extra_test_func(self):
        return self.object.practice.supervisor_practice == self.request.user.supervisorpractice

    def get_success_url(self):
        return reverse('supervisor-practice-practice-student-detail', kwargs={'pk': self.object.id})
    
