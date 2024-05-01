from user.models import (
    DirectionOfTraining,
    Group,
    Practice,
    PracticeStudent,
)

def get_queryset_practice_student_for_SupervisorPractice(supervisorpractice):
    practice = Practice.objects.filter(supervisor_practice=supervisorpractice)
    
    if not practice:
        return PracticeStudent.objects.none()
    
    return PracticeStudent.objects.filter(practice__in=practice)

    

def get_queryset_group_for_SupervisorPractice(supervisorpractice):
    practice_student = get_queryset_practice_student_for_SupervisorPractice(supervisorpractice)
    
    if not practice_student:
        return Group.objects.none()
    
    student_ids = practice_student.values_list('student_id', flat=True)
    return Group.objects.filter(student__in=student_ids).distinct()


def get_queryset_direction_of_training_for_SupervisorPractice(supervisorpractice):
    groups = get_queryset_group_for_SupervisorPractice(supervisorpractice)

    if not groups:
        return DirectionOfTraining.objects.none()
    
    return DirectionOfTraining.objects.filter(group__in=groups).distinct()
