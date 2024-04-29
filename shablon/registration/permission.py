from supervisorOPOP.models import (
    SupervisorOPOP,
)
from supervisorPractice.models import (
    SupervisorPractice,
)
from student.models import (
    Student,
    Group,
)

def isStudent(user):
    return Student.objects.filter(user=user).exists()


def isSupervisorOPOP(user):
    return SupervisorOPOP.objects.filter(user=user).exists()


def isSupervisorPractice(user):
    return SupervisorPractice.objects.filter(user=user).exists()
