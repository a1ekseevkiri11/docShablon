from django.contrib.auth.mixins import (
    LoginRequiredMixin, 
    UserPassesTestMixin
)

from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from docxtpl import DocxTemplate

from registration.permission import isStudent




class StudentMixin(LoginRequiredMixin, UserPassesTestMixin):
    
    def test_func(self):
        return isStudent(self.request.user)


