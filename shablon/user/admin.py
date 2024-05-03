from django.contrib import admin

from .models import (
    Amount,
    DirectionOfTraining,
    Group,
    Institute,
    Practice,
    PracticeStudent,
    RatingPracticeStudent,
    StudentProductionTasks,
)

admin.site.register(Amount)

class DirectionOfTrainingAdmin(admin.ModelAdmin):
    filter_horizontal = ('supervisorOPOP',)

admin.site.register(DirectionOfTraining, DirectionOfTrainingAdmin)


    
admin.site.register(Group)
admin.site.register(Institute)

class PracticeAdmin(admin.ModelAdmin):
    filter_horizontal = ('group',)

admin.site.register(Practice, PracticeAdmin)

admin.site.register(PracticeStudent)

admin.site.register(RatingPracticeStudent)
admin.site.register(StudentProductionTasks)

