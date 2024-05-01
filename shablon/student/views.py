from django.contrib.auth.mixins import (
    LoginRequiredMixin, 
    UserPassesTestMixin
)

from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

from django.views.generic import (
    ListView,
    DetailView,
    View,
    CreateView,
    UpdateView,
    DeleteView,
    ListView
)

from registration.permission import isStudent

from user.models import (
    PracticeStudent,
    Practice,
)

from django.shortcuts import render, get_object_or_404

from .forms import (
    PracticeStudentFormStudent,
)

from django.urls import (
    reverse_lazy,
    reverse,
)

from django.http import HttpResponseRedirect




class StudentMixin(LoginRequiredMixin, UserPassesTestMixin):
    
    def test_func(self):
        return isStudent(self.request.user)



class PracticeListView(ListView, StudentMixin):
    template_name = 'student/practice_list.html' 
    context_object_name = 'practices'

    def get_queryset(self):
        return Practice.objects.filter(group=self.request.user.student.group)
    

class PracticeDetailView(View, StudentMixin):
    template_name = 'student/practice_detail.html' 

    
    def get(self, request, pk):
        practice = get_object_or_404(Practice, pk=pk)
        context = {}
        context['practice'] = practice

        try:
            practice_student = PracticeStudent.objects.get(practice=practice)
        except PracticeStudent.DoesNotExist:
            practice_student = None

        context['practice_student'] = practice_student
        return render(request, self.template_name, context)



class PracticeStudentCreateView(CreateView):
    model = PracticeStudent
    template_name = 'student/practice_student_form.html'
    form_class = PracticeStudentFormStudent

    def form_valid(self, form):
        self.object = form.save(commit=False)
        practice_id = self.kwargs['practice_pk']
        practice = get_object_or_404(Practice, pk=practice_id)
        self.object.practice = practice
        self.object.student = self.request.user.student
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
    
    def get_success_url(self):
        practice_id = self.kwargs['practice_pk']
        return reverse('student-practice-detail', kwargs={'pk': practice_id})


class PracticeStudentUpdateView(UpdateView, StudentMixin):
    model = PracticeStudent
    template_name = 'student/practice_student_form.html'
    form_class = PracticeStudentFormStudent

    def form_valid(self, form):
        self.object = form.save(commit=False)
        practice_id = self.kwargs['practice_id']
        practice = get_object_or_404(Practice, pk=practice_id)
        self.object.practice = practice
        self.object.student = self.request.user.student
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        practice_id = self.kwargs['practice_id']
        return reverse('student-practice-detail', kwargs={'pk': practice_id})