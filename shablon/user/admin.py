from django.contrib import admin

from .models import (
    Amount,
    DirectionOfTraining,
    Group,
    Institute,
    Practice,
    PracticeStudent,
)

admin.site.register(Amount)

class DirectionOfTrainingAdmin(admin.ModelAdmin):
    filter_horizontal = ('supervisorOPOP',)

admin.site.register(DirectionOfTraining, DirectionOfTrainingAdmin)

class GroupAdmin(admin.ModelAdmin):
    filter_horizontal = ('direction_of_training',)
    
admin.site.register(Group, GroupAdmin)
admin.site.register(Institute)
admin.site.register(Practice)
admin.site.register(PracticeStudent)
