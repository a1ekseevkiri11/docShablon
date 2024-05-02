from django.contrib.auth.mixins import (
    LoginRequiredMixin, 
    UserPassesTestMixin
)

from io import BytesIO
from docxtpl import DocxTemplate

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
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


def practice_student_test_func(practice_student, student):
    return practice_student.student == student



class StudentMixin(LoginRequiredMixin, UserPassesTestMixin):

    def extra_test_func(self):
        return True
    
    def test_func(self):
        return isStudent(self.request.user) and self.extra_test_func()



class PracticeListView(ListView, StudentMixin):
    template_name = 'student/practice_list.html' 
    context_object_name = 'practices'
    paginate_by = 1

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
    

    def post(self, request, pk):
        practice = get_object_or_404(Practice, pk=pk)
        context = {}
        context['practice'] = practice

        try:
            practice_student = PracticeStudent.objects.get(practice=practice)

        except PracticeStudent.DoesNotExist:
            return HttpResponseBadRequest("Нет отчета")
        
        if not practice_student.amount:
            return HttpResponseBadRequest("Нет оценки отчета")
        
        
        context = {
            'practice': practice, 
            'practice_student': practice_student,
        }

        print(practice.get_kind_display)

        tpl = DocxTemplate("C://Users//79828//Desktop//docShablon//shablon//student//shablon//practice_diary_template.docx")
        tpl.render(context)
        output = BytesIO()
        tpl.save(output)
        output.seek(0)
        response = HttpResponse(output.read(), content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
        response['Content-Disposition'] = f'attachment; filename="generated_report.docx"'

        return response



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
    
    def extra_test_func(self):
        return practice_student_test_func(self.object, self.request.user.student)
    
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
    
    def extra_test_func(self):
        return practice_student_test_func(self.object, self.request.user.student)

    def get_success_url(self):
        practice_id = self.kwargs['practice_id']
        return reverse('student-practice-detail', kwargs={'pk': practice_id})
    


