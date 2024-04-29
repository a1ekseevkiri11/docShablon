from django.contrib import admin


from .models import(
    Institute,
    DirectionOfTraining,
    Group
)


admin.site.register(Institute)
admin.site.register(DirectionOfTraining)
admin.site.register(Group)

