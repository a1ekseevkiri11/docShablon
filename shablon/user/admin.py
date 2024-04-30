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
admin.site.register(DirectionOfTraining)
admin.site.register(Group)
admin.site.register(Institute)
admin.site.register(Practice)
admin.site.register(PracticeStudent)
