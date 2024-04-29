from django.shortcuts import render

from django.contrib.auth.mixins import (
    LoginRequiredMixin, 
    UserPassesTestMixin
)

from registration.permission import isSupervisorOPOP


class SupervisorOPOPMixin(LoginRequiredMixin, UserPassesTestMixin):
    
    def test_func(self):
        return isSupervisorOPOP(self.request.user)

