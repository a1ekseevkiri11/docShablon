from django.shortcuts import render

from django.contrib.auth.mixins import (
    LoginRequiredMixin, 
    UserPassesTestMixin
)

from registration.permission import isSupervisorPractice


class SupervisorPracticeMixin(LoginRequiredMixin, UserPassesTestMixin):
    
    def test_func(self):
        return isSupervisorPractice(self.request.user)