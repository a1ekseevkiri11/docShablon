from django.shortcuts import render

from django.contrib.auth.mixins import (
    LoginRequiredMixin, 
    UserPassesTestMixin
)

from django.urls import (
    reverse_lazy,
    reverse,
)


from django.db.models import Q

from django.http import JsonResponse

from django.views.generic import (
    DetailView,
    View,
    CreateView,
    UpdateView,
    DeleteView,
    ListView
)

from user.models import (
    DirectionOfTraining,
    Group,
    Practice,
)

from .filters import PracticeFilter

from registration.permission import isSupervisorOPOP

from .forms import PracticeForm

from .queryset import (
    get_queryset_practice_for_SupervisorOPOP,
    
)

def get_groups(request):
    direction_id = request.GET.get('direction_id')  # Получаем id выбранного направления обучения
    groups = Group.objects.filter(direction_of_training=direction_id)  # Фильтруем группы по выбранному направлению обучения
    data = [{'id': group.id, 'title': group.title} for group in groups]  # Преобразуем группы в формат JSON
    return JsonResponse({'groups': data})


def practice_test_func(practice, supervisoropop):
    practice = get_queryset_practice_for_SupervisorOPOP(supervisoropop)
    return practice.filter(id=practice.id).exists()


class SupervisorOPOPMixin(LoginRequiredMixin, UserPassesTestMixin):

    def extra_test_func(self):
        return True
    
    def test_func(self):
        return isSupervisorOPOP(self.request.user) and self.extra_test_func()
    

class PracticesListView(ListView, SupervisorOPOPMixin):
    template_name = 'supervisorOPOP/practice_list.html'
    context_object_name = 'practices'
    paginate_by = 1


    def get_queryset(self):
        
        queryset = get_queryset_practice_for_SupervisorOPOP(self.request.user.supervisoropop)
        query = self.request.GET.get('q')
        filters = self.request.GET
        
        if query:
            queryset = queryset.filter(Q(title__icontains=query))
        
        self.filterset = PracticeFilter(filters, queryset=queryset, supervisoropop=self.request.user.supervisoropop,)
        return self.filterset.qs
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filters'] = self.filterset.form
        context['applied_filters'] = self.request.GET.urlencode()
        return context
    

class PracticesDetailView(DetailView, UserPassesTestMixin):
    model = Practice
    template_name = 'supervisorOPOP/practice_detail.html'
    context_object_name = 'practice'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)            
        return context


class PracticeCreateView(CreateView, SupervisorOPOPMixin):

    template_name = 'supervisorOPOP/practice_new.html'
    form_class = PracticeForm 
    success_url = reverse_lazy('practice-list')
    context_object_name = 'practice'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)   
        context['direction_of_training'] = self.request.user.supervisoropop.directionoftraining_set.all()
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['supervisoropop'] = self.request.user.supervisoropop  # Передаем текущего пользователя в параметрах формы
        return kwargs



class PracticeUpdateView(UpdateView, SupervisorOPOPMixin):
    model = Practice
    template_name = 'supervisorOPOP/practice_update.html'
    form_class = PracticeForm
    context_object_name = 'practice'

    def extra_test_func(self):
        return practice_test_func(self.object, self.request.user.supervisoropop)
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)   
        context['direction_of_training'] = self.request.user.supervisoropop.directionoftraining_set.all()
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['supervisoropop'] = self.request.user.supervisoropop  # Передаем текущего пользователя в параметрах формы
        kwargs['instance'] = self.object  # Передаем объект для обновления
        return kwargs
    
    def get_success_url(self):
        return reverse('practice-detail', kwargs={'pk': self.object.pk})


class PracticeDeleteView(DeleteView, SupervisorOPOPMixin):
    model = Practice
    template_name = 'supervisorOPOP/practice_delete.html'
    success_url = reverse_lazy('practice-list')
    context_object_name = 'practice'

    def extra_test_func(self):
        return practice_test_func(self.object, self.request.user.supervisoropop)

    



class DirectionOfTrainingDetailView(DetailView, SupervisorOPOPMixin):
    model = DirectionOfTraining
    template_name = 'supervisorOPOP/direction_of_training_detail.html'
    context_object_name = 'direction'
