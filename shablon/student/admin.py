from django.contrib import admin


from .models import(
    Institute,
    DirectionOfTraining,
    Group,
    Student,
    PracticeStudent,
    Amount,
)

admin.site.register(Student)
admin.site.register(Institute)
admin.site.register(DirectionOfTraining)
admin.site.register(Group)
admin.site.register(PracticeStudent)
admin.site.register(Amount)
