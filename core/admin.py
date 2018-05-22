from django.contrib import admin

from .models import Classroom, Student, List, Subject, Task, StudClass


# Register your models here.
#admin.site.register(User)
admin.site.register(StudClass )
admin.site.register(Classroom)
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(List)
admin.site.register(Task)