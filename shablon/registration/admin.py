from django.contrib import admin

from .models import(
    Student,
    SupervisorPractice,
    SupervisorOPOP
)


admin.site.register(Student)
admin.site.register(SupervisorOPOP)
admin.site.register(SupervisorPractice)