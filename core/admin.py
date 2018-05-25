from django.contrib import admin

from .models import Classroom, Student, List, Subject, Task, StudClass

class StudClassAdmin(admin.ModelAdmin):
    list_display=('date', 'daily_attendance', 'classroom', 'display_students')

    def display_students(self, obj):
        p = Student.objects.filter(studclass=obj.pk)
        return list(p)    

# Register your models here.
#admin.site.register(User)
admin.site.register(StudClass, StudClassAdmin )
admin.site.register(Classroom)
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(List)
admin.site.register(Task)